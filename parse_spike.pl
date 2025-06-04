#!/usr/bin/env perl

use strict;
use warnings;
use 5.012;
use Data::Dumper;

use open qw( :std :encoding(UTF-8) );

use Cwd qw/abs_path/;
use File::Basename qw/dirname/;
#use HTML::Parser;
use Mojo::DOM58;

my $fn_in = $ARGV[0];
my $base_dir = dirname(abs_path($fn_in));

my $html;
open my $in, '<', $fn_in;
while (my $line = <$in>) {
    $html .= $line;
}
close $in;
my $dom = Mojo::DOM58->new($html);


my $l2 =
#'base__------packages-flipper-web-src-components-app-page-app-page-module';
'base';
my $s1 =
'__------packages-flipper-web-src-components-app-page-app-page-module';
my $s2 =
'__------packages-flipper-web-src-components-app-page-app-page-content-module';

for my $node ($dom->descendant_nodes->each) {
    my $class = $node->attr('class') // next;
    $class =~ s/$s1//g;
    $class =~ s/$s2/.content/g;
    $node->attr({class => $class});
}
for my $link ($dom->find('a[href^="https://spike.legoeducation.com/prime/help/lls-help-python"]')->each) {
    my $href = $link->attr('href');
    $href =~ s/^.+#/#/;
    $link->attr({'href' => $href});
}
for my $code ($dom->find('code')->each) {
    $code->attr({'class' => 'language-python'});
}
for my $button ($dom->find('button')->each) {
    $button->remove();
}
for my $ht (qw/h4 h5/) {
    for my $header ($dom->find($ht)->each) {
        my $c = $header->content;
        $c =~ s/^\s+|\s+$//;
        next if ($c ne 'Functions');
        for my $next ($header->parent->following('div')->each) {
            my $children = $next->children($ht) // last;
            my $c = $children->first;
            $c = $c->content;
            $c =~ s/^\s+|\s+$//;
            last if ($c eq 'Constants');
            $next->attr({'class' => join(' ', $next->attr('class'), 'function')});
            warn "$c\n";
        }
    }
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
my $root = $dom->at(sprintf('div[class~="%s"]', $l2));
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

    for my $child ( $el->children(sprintf('div[class~="%s"]', $l2))->each ) {
        
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
