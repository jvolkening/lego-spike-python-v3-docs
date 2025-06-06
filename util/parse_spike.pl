#!/usr/bin/env perl

use strict;
use warnings;
use 5.012;
use autodie;
use open qw( :std :encoding(UTF-8) );

use Cwd qw/abs_path/;
use Data::Dumper;
use File::Basename qw/dirname/;
use File::Path qw/make_path/;
use Getopt::Long;
use HTML::Entities;
use HTML::WikiConverter;
use Mojo::DOM58;
use Text::Wrap;

$Text::Wrap::unexpand = 0;

my $fi_html;
my $dir_stubs;
my $original_source = "https://spike.legoeducation.com/prime/help/lls-help-python";
my $fo_dump;

GetOptions(
    '--in=s'     => \$fi_html,
    '--stubs=s'  => \$dir_stubs,
    '--source=s' => \$original_source,
    '--dump=s'   => \$fo_dump,
);

my $tab = '    ';
my %extra_imports = (
    motor_pair => [
        'import motor'
    ],
);

# read in DOM
my $html;
open my $in, '<', $fi_html;
while (my $line = <$in>) {
    $html .= $line;
}
close $in;
my $dom = Mojo::DOM58->new($html);

# do some intial cleanup
clean_cruft($dom);
rename_classes($dom);
make_links_relative($dom);
relevel_submodules($dom);
strip_constant_headers($dom);

my $api_heading = 'API Modules';
my $api_root = get_div_with_heading(
    $dom,
    2,
    $api_heading,
) // die "Nothing found for '$api_heading'\n";

my $api_tree = parse_api($api_root);

dump_tree($api_tree, $fo_dump)
    if (defined $fo_dump);

if (defined $dir_stubs) {
    generate_stubs($api_tree, $dir_stubs);
}

my $new = Mojo::DOM58->new('<html><head></head><body></body>');
$new->at('head')->append_content( $dom->new_tag(
    'link',
    'href' =>
    "https://fonts.googleapis.com/css2?family=Inconsolata:wght@200..900&display=swap",
    'rel' => "stylesheet",
));
$new->at('head')->append_content( $dom->new_tag(
    'link',
    'href' => 'spike.css',
    'rel' => 'stylesheet',
));
my $root = $dom->at('div[class~="base"]');
$root->attr({id => 'main-content'});
my @menu_items = traverse($root);
my $menu = $dom->new_tag(
    'ol',
    id => 'main-menu',
);
for my $item (@menu_items) {
    $menu->at('ol')->append_content($item);
}
$root->at('h1')->content('Python and the Spike Prime Hub (v3)');
$new->at('body')->append_content($menu);
$new->at('body')->append_content($root);

say "$new";

sub traverse {

    my ($el) = @_;

    my @children;

    for my $child ( $el->children('div[class~="base"]')->each ) {
        
        my $a = $child->at('a[id]');
        my $id = $a->attr('id');
        my $header = $child->at('h1')
            // $child->at('h2')
            // $child->at('h3');
        next if (! defined $header);
        my $name = $header->content;
        $name =~ s/^\s*//g;
        $name =~ s/\s$//g;
        my @kids = traverse($child);
        my $item = $dom->new_tag(
            'li', 
        );
        $item->at('li')->append_content($dom->new_tag(
                'a',
                'href' => "#$id",
                $name
            )
        );
        if (scalar @kids) {
            my $submenu = $dom->new_tag(
                'ol',
                class => join('-', $header->tag, 'menu'),
            );
            for my $kid (@kids) {
                $submenu->at('ol')->append_content($kid);
            }
            $item->at('li')->append_content($submenu);
        }
                
        push @children, $item;

    }

    return @children;

}

sub clean_cruft {

    my ($dom) = @_;
    for my $hr ($dom->find('hr')->each) {
        $hr->parent->remove;
    }
    for my $button ($dom->find('button')->each) {
        $button->remove();
    }

}

sub strip_constant_headers {

    my ($dom) = @_;
    for my $h ($dom->find('h4[class~="heading"]')->each) {
        my $v = get_value($h);
        next if ($v ne 'Constants');
        $h->parent->remove;
    }

}

sub get_value {

    my ($el) = @_;
    my $content = $el->content;
    $content =~ s/^\s+|\s+$//;
    return decode_entities("$content");

}

sub rename_classes {

    my ($dom) = @_;

    my $s1 = '__------packages-flipper-web-src-components-app-page-app-page-module';
    my $s2 = '__------packages-flipper-web-src-components-app-page-app-page-content-module';

    for my $node ($dom->descendant_nodes->each) {
        my $class = $node->attr('class') // next;
        $class =~ s/$s1//g;
        $class =~ s/$s2/.content/g;
        $node->attr({class => $class});
    }

}

sub make_links_relative {

    my ($dom) = @_;
    for my $link ($dom->find(sprintf('a[href^="%s"]', $original_source))->each) {
        my $href = $link->attr('href');
        $href =~ s/^.+#/#/;
        $link->attr({'href' => $href});
    }

}

sub relevel_submodules {

    my ($dom) = @_;

    for my $header ($dom->find('h4')->each) {
        my $c = $header->content;
        $c =~ s/^\s+|\s+$//;
        next if ($c ne 'Sub Modules');
        my $module = $header->parent->parent->at('h3')->content;
        $module =~ s/^\s+|\s+$//;
        my @extra;
        my $parent = $header->parent->parent;
        for my $child ($parent->find('h4')->each) {
            my $c = $child->content;
            $c =~ s/^\s+|\s+$//;
            next if ($c ne 'Functions');
            push @extra, $child->parent;
            for my $other ($child->parent->following('div[class="base"]')->each) {
                push @extra, $other;
                $other->remove;
            }
            $child->parent->remove;
        }
        SIBLING:
        for my $sibling ($header->parent->following('div[class="base"]')->each) {
            for my $ht (qw/4/) {
                my $old = "h$ht";
                my $new = sprintf "h%s", $ht-1;
                for my $child ($sibling->find($old)->each) {
                    my $c = $child->content;
                    $c =~ s/^\s+|\s+$//;
                    last SIBLING if ($c eq 'Functions');
                    $child->tag($new);
                }
            }
            for my $ht (qw/5 6/) {
                my $old = "h$ht";
                my $new = sprintf "h%s", $ht-1;
                for my $child ($sibling->find($old)->each) {
                    my $c = $child->content;
                    $c =~ s/^\s+|\s+$//;
                    $child->tag($new);
                }
            }
            for my $child ($sibling->children('h3')->each) {
                my $curr = $child->content;
                $curr =~ s/^\s+|\s+$//;
                $child->content("$module.$curr");
            }
        }
        $header->parent->remove;
        $parent->at('h3')->append($_) for (reverse @extra);
    }
}

sub get_div_with_heading {

    my ($dom, $level, $value) = @_;

    for my $h ($dom->find(sprintf('h%s[class="heading"]', $level))->each) {
        next if (get_value($h) ne $value);
        return $h->parent;
    }
    return undef;

}

sub add_class {

    my ($el, $class) = @_;
    $el->attr({
        'class' => join(
            ' ',
            ($el->attr('class') // ''),
            $class
        )
    });

}

sub parse_api {

    my ($root) = @_;

    my $tree;

    for my $module ($root->children('div[class~="base"]')->each) {
        add_class( $module, 'api-module' );
        my @objs = parse_module($module);
        push @{$tree}, @objs;
    }

    return $tree;

}

sub parse_module {

    my ($module, $parent) = @_;
    my $obj = {};

    my @objs = ();
   
    $obj->{name} = lc get_value( $module->at('h3') )
        // die "No name found for class";
    $obj->{parent} = $parent; # maybe undef
    $obj->{docs} = [];
    $obj->{functions} = [];
    $obj->{constants} = [];

    # first check for submodules
    for my $it ($module->children->each) {
        next if (! scalar $it->children('h3')->each); 
        add_class( $it, 'api-module' );
        push @objs, parse_module($it, $obj->{name});
    }
    my $curr_type; # track functions and constants
    for my $it ($module->children()->each) {
        next if (scalar $it->children('h3')->each); 
        # extract textual documentation chunks
        if ($it->matches('div[class~="text.content"]')) {
            push @{ $obj->{docs} }, {
                type => 'text',
                content => get_value($it)
            };
            add_class( $it, 'api-module-description' );
        }
        # extract code block chunks
        elsif ($it->matches('pre[class~="code.content"]')) {
            push @{ $obj->{docs} }, {
                type => 'code_block',
                content => "$it",
            };
            add_class( $it, 'api-module-example' );
        } # parse function and constant lists
        elsif ($it->matches('div[class~="base"]')) { 
            my $name = my $h = $it->children('h4')->first;
            die "No h4 found for $obj"
                if (! defined $name);
            $name = get_value($name);
            if ($name eq 'Functions') {
                $curr_type = 'functions';
                add_class( $it, 'api-functions-heading' );
                next;
            }
            elsif ($name =~ /\bConstants$/) {
                $curr_type = 'constants';
                push @{ $obj->{constants}}, parse_constants($it);
                add_class( $it, 'api-constants' );
                next;
            }
            elsif ($curr_type eq 'functions') {
                push @{ $obj->{functions}}, parse_function($it);
                add_class( $it, 'api-function' );
            }
            elsif ($curr_type eq 'constants') {
                push @{ $obj->{constants}}, parse_constants($it);
                add_class( $it, 'api-constants' );
            }
        }
    }
    push @objs, $obj;

    return @objs;

}

sub block_to_markdown {

    my ($el) = @_;

    my $wc = new HTML::WikiConverter( dialect => 'Markdown' );
    return $wc->html2wiki( "$el" );

}

sub parse_function {

    my ($el) = @_;

    my $obj = {};
   
    $obj->{name} = lc get_value( $el->at('h4') )
        // die "No name found for function";
    $obj->{docs} = [];
    $obj->{parameters} = [];

    my $curr_type; # track functions and constants
    for my $it ($el->children()->each) {
        # extract textual documentation chunks
        if ($it->matches('div[class~="text.content"]')) {
            if (! defined $obj->{definition}) {
                $obj->{definition} = get_value($it->at('p'));
            add_class( $it, 'api-function-definition' );
            }
            else {
                push @{ $obj->{docs} }, {
                    type => 'text',
                    content => get_value($it)
                };
                add_class( $it, 'api-function-description' );
            }
        }
        # extract code block chunks
        elsif ($it->matches('pre[class~="code.content"]')) {
            push @{ $obj->{docs} }, {
                type => 'code_block',
                content => "$it",
            };
            add_class( $it, 'api-function-example' );
        } # parse function and constant lists
        elsif ($it->matches('div[class~="base"]')) { 
            my $name = get_value($it->children('h5')->first)
                // die "No h4 found for $obj";
            if ($name eq 'Parameters') {
                $curr_type = 'parameters';
                add_class( $it, 'api-parameter-heading' );
                next;
            }
            elsif ($curr_type eq 'parameters') {
                next if (! defined $it->children('div[class~="text.content"]')->first);
                push @{ $obj->{parameters}}, parse_parameter($it);
                add_class( $it, 'api-parameter' );
            }
        }
    }

    return $obj;

}

sub parse_parameter {

    my ($el) = @_;

    my $obj = {};
    
    $obj->{name} = lc get_value( $el->at('h5') )
        // die "No name found for parameter";
    ($obj->{param}, $obj->{type}) = split /:\s*/, $obj->{name}, 2;
    $obj->{docs} = [];

    my $curr_type; # track functions and constants
    for my $it ($el->children()->each) {
        # extract textual documentation chunks
        if ($it->matches('div[class~="text.content"]')) {
            push @{ $obj->{docs} }, {
                type => 'text',
                content => get_value($it)
            };
            add_class( $it, 'api-parameter-description' );
        }
        # extract code block chunks
        elsif ($it->matches('pre[class~="code.content"]')) {
            push @{ $obj->{docs} }, {
                type => 'code_block',
                content => "$it",
            };
            add_class( $it, 'api-parameter-example' );
        }
    }

    return $obj;

}

sub parse_constants {

    my ($el) = @_;

    my @consts;

    for my $it ($el->children()->each) {
        # extract textual documentation chunks
        if ($it->matches('div[class~="text.content"]')) {
            for my $p ($it->children('p')->each) {
                my $k = get_value($p->at('strong'))
                    // die "No key found for $p";
                my $v = get_value($p);
                $v =~ s/.+=\s*//;
                $v =~ s/[^\d\-].*$//;
                push @consts, {
                    key => $k,
                    val => $v
                };
                add_class( $p, 'api-constant' );
            }
        }
    }

    return @consts;

}

sub generate_stubs {

    my ($tree, $dir_out) = @_;

    if (-e $dir_out && ! -d $dir_out) {
        die "Output directory $dir_out exists but is not directory\n";
    }
    make_path($dir_out)
        if (! -e $dir_out);
    for my $module (@{ $tree }) {
        my $name = $module->{name};
        $name =~ s/.+\.//;
        $name =~ s/\s/_/g;
        my $dir = $dir_out;
        if (defined $module->{parent}) { #submodule
            $dir = "$dir_out/$module->{parent}";
            make_path($dir)
                if (! -e $dir);
            if (! -e "$dir/__init__.py") {
                open my $out, '>', "$dir/__init__.py";
                close $out;
            }
        }
        my $fn = "$dir/$name.py";
        open my $out, '>', $fn;


        my $doc = make_doc($module);
        say {$out} "\"\"\"";
        #$doc =~ s/^\K/$tab/gm;
        print {$out} $doc;
        say {$out} "\"\"\"\n";

        my @imports;
        for my $kw (qw/Awaitable Callable/) {
            if (
                grep {$_ =~ /\b$kw\b/}
                map {$_->{definition}}
                @{ $module->{functions} }
            ) {
                push @imports, "from typing import $kw";
            }
        }
        if (defined $extra_imports{$name}) {
            push @imports, @{ $extra_imports{$name} };
        }
        say {$out} join( "\n", @imports), "\n"
            if (scalar @imports);

        my @constants = @{ $module->{constants} };
        if (scalar @constants) {
            for my $const (@constants) {
                say {$out} "$const->{key} = $const->{val}";
            }
            print {$out} "\n";
        }

        #generate function docstrings
        for my $func (@{ $module->{functions} }) {
            my $def = $func->{definition};
            while ($def =~ s/\[[^\]]+\]//g) {
                next;
            }
            $def =~ s/\:\s*\w+//g;
            my $return;
            if ($def =~ /(.+?)\s*->\s*(\S+)/) {
                $def = $1;
                $return = $2;
            }
            #if ($func->{definition} =~ /\bAwaitable$/) {
                #print {$out} 'async ';
            #}

            # clean up the function definition a bit to pass linting
            my $def_string = $func->{definition};
            $def_string =~ s/^\w+ //g;
            $def_string =~ s/ $name\./ /g;

            # fix function definition type hints like the following:
            #def set_pixel(port: int, x: int, y: int, pixel: tuple[color: int, intensity: int]) -> None:
            while ($def_string =~ /^(.+?\btuple\[)([^\]]+)(\].*)$/g) {
                my $prev = $def_string;
                my ($s, $m, $e) = ($1, $2, $3);
                $m =~ s/\b\w+: //g;
                $def_string = "$s$m$e";
                last if ($def_string eq $prev);
            }

            say {$out} "def $def_string:";
            my $desc = '';
            #my $desc = join '',
                #map {$_->{content}}
                #grep {$_->{type} eq 'text'}
                #@{ $func->{docs} };
            for my $part (@{ $func->{docs} }) {
                if ($part->{type} eq 'text') {
                    $desc .= wrap('','',block_to_markdown("$part->{content}")) . "\n";
                }
                elsif ($part->{type} eq 'code_block') {
                    my $code = block_to_markdown("$part->{content}");
                    $code =~ s/^\s*\K\`//;
                    $code =~ s/`\s*$//;
                    #$code =~ s/^\K/$tab/gm;
                    $desc .= "\n::\n\n$code\n";
                }
            }
            $desc =~ s/^\K/$tab/gm;
            $desc =~ s/<br \/>\s*/ /gm;
            say {$out} "$tab\"\"\"\n$desc";

            for my $param (@{ $func->{parameters} }) {
                my $desc = join '',
                    map {$_->{content}}
                    grep {$_->{type} eq 'text'}
                    @{ $param->{docs} };
                $desc = block_to_markdown($desc)
                    if (length $desc);
                $desc =~ s/\n//gm;
                if ($param->{param} =~ /^\*/) {
                    $desc = "A tuple of " . lcfirst($desc);
                    $param->{param} =~ s/^\*//g;
                }
                $desc =~ s/<br \/>\s*/ /gm;
                say {$out} wrap($tab, "$tab$tab", ":param $param->{param}: $desc");
            }
            say {$out} "$tab:rtype: $return";
            say {$out} "$tab\"\"\"\n";
            # apparently pass is not needed if we have docstrings
            #say {$out} "${tab}pass\n";

        }
    }
}

sub make_doc {

    my ($el) = @_;

    my $desc = '';
    for my $part (@{ $el->{docs} }) {
        if ($part->{type} eq 'text') {
            $desc .= wrap('','',block_to_markdown("$part->{content}")) . "\n\n";
        }
        elsif ($part->{type} eq 'code_block') {
            my $code = block_to_markdown("$part->{content}");
            $code =~ s/^\s*\K\`//;
            $code =~ s/`\s*$//;
            #$code =~ s/^\K/$tab/g;
            $desc .= "::\n\n$code\n\n";
        }
    }

    my @constants = defined $el->{constants}
        ? @{ $el->{constants} }
        : ();
    if (scalar @constants) {
        $desc .= "\nThe following constants are defined:\n\n";
        for my $const (@constants) {
            $desc .= "* $const->{key} = $const->{val}\n"
        }
    }

    $desc =~ s/<br \/>\s*/ /gm;
    chomp $desc;
    return $desc;

}

sub dump_tree {

    my ($obj, $fn) = @_;
    
    open my $out, '>', $fn;
    print {$out} Dumper $obj;
    close $out;

}

