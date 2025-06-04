<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:outline="http://wkhtmltopdf.org/outline"
                xmlns="http://www.w3.org/1999/xhtml">
    <xsl:output doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
                doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitiona
l.dtd"
                indent="yes" />
    <xsl:template match="outline:outline">
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <style>
                    body {font-family: "Lato", "sans-serif";}
                    p.h2 {
                    font-size: 26;
                    font-weight: 700;
                    }
                    div {border-bottom: 1px dashed rgb(200,200,200);}
                    span {float: right;}
                    li {list-style: none; padding-top: 10px;}
                    ul {
                    font-size: 20;
                    }
                    ul ul {font-size: 80%; }
                    ul {padding-left: 0em;}
                    ul ul {padding-left: 1em;}
                    a {text-decoration:none; color: black;}
                    div.h1 {
                    font-size: 40px;
                    border: solid 1px black;
                    padding: 20px;
                    text-align: center;
                    }
                </style>
            </head>
            <body>
                <div class="h1">Python and the Spike Prime Hub (v3)</div>
                <p class="h2">Table of Contents</p>
                <ul><xsl:apply-templates select="outline:item/outline:item"/></ul>
            </body>
        </html>
    </xsl:template>
    <xsl:template match="outline:item/outline:item" priority="0" />
    <xsl:template match="outline:item" priority="1">
        <xsl:if test="count(ancestor::*) &lt; 4">
        <li>
            <xsl:if test="@title!=''">
                <div>
                    <a>
                        <xsl:if test="@link">
                            <xsl:attribute name="href"><xsl:value-of select="@link"/></xsl:attribute>
                        </xsl:if>
                        <xsl:if test="@backLink">
                            <xsl:attribute name="name"><xsl:value-of select="@backLink"/></xsl:attribute>
                        </xsl:if>
                        <xsl:value-of select="@title" />
                    </a>
                    <span> <xsl:value-of select="@page" /> </span>
                </div>
            </xsl:if>
            <ul>
                <xsl:comment>added to prevent self-closing tags in QtXmlPatterns</xsl:comment>
                <xsl:apply-templates select="outline:item"/>
            </ul>
        </li>
        </xsl:if>
    </xsl:template>
</xsl:stylesheet>
