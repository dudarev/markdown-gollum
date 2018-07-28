"""
Regressions tests.

Copied from wikilinks Python-Markdown tests to make sure that they still pass.
They may be found in Python-Markdown repo at:

markdown/tests/test_extensions.py

`testLinkText` test is added.
"""

import unittest

import markdown

from markdown_gollum import wikilinks


class TestWikiLinks(unittest.TestCase):
    """ Test Wikilinks Extension. """

    def setUp(self):
        self.md = markdown.Markdown(extensions=[wikilinks.WikiLinkExtension()])
        self.text = "Some text with a [[WikiLink]]."

    def testBasicWikilinks(self):
        """ Test [[wikilinks]]. """

        self.assertEqual(
            self.md.convert(self.text),
            '<p>Some text with a '
            '<a class="wikilink" href="/WikiLink/">WikiLink</a>.</p>'
        )

    def testWikilinkWhitespace(self):
        """ Test whitespace in wikilinks. """
        self.assertEqual(
            self.md.convert('[[ foo bar_baz ]]'),
            '<p><a class="wikilink" href="/foo-bar_baz/">foo bar_baz</a></p>'
        )
        self.assertEqual(
            self.md.convert('foo [[ ]] bar'),
            '<p>foo  bar</p>'
        )

    def testWikilinkWithCommas(self):
        self.assertEqual(
            self.md.convert('[[Подскажите, пожалуйста, кто в городе плетёт косы с канеколоном, кроме Серафимы.|facebook-2001100099931047]]'),  # noqa
            '<p><a class="wikilink" href="/facebook-2001100099931047/">Подскажите, пожалуйста, кто в городе плетёт косы с канеколоном, кроме Серафимы.</a></p>'  # noqa
        )
        self.assertEqual(
            self.md.convert('foo [[ ]] bar'),
            '<p>foo  bar</p>'
        )

    def testPunctuation(self):
        self.assertEqual(
            self.md.convert('[[?!|facebook-2001100099931047]]'),
            '<p><a class="wikilink" href="/facebook-2001100099931047/">?!</a></p>'
        )
        self.assertEqual(
            self.md.convert('foo [[ ]] bar'),
            '<p>foo  bar</p>'
        )

    def testSimpleSettings(self):
        """ Test Simple Settings. """

        self.assertEqual(
            markdown.markdown(
                self.text, extensions=[
                    wikilinks.WikiLinkExtension(
                        base_url='/wiki/',
                        end_url='.html',
                        html_class='foo')
                ]
            ),
            '<p>Some text with a '
            '<a class="foo" href="/wiki/WikiLink.html">WikiLink</a>.</p>')

    def testComplexSettings(self):
        """ Test Complex Settings. """

        md = markdown.Markdown(
            extensions=[wikilinks.WikiLinkExtension(
                base_url='http://example.com/',
                end_url='.html',
                html_class=''
            )]
        )
        self.assertEqual(
            md.convert(self.text),
            '<p>Some text with a '
            '<a href="http://example.com/WikiLink.html">WikiLink</a>.</p>'
        )

    def testWikilinksMetaData(self):
        """ test MetaData with Wikilinks Extension. """

        text = """wiki_base_url: http://example.com/
wiki_end_url:   .html
wiki_html_class:

Some text with a [[WikiLink]]."""
        md = markdown.Markdown(
            extensions=['markdown.extensions.meta', wikilinks.WikiLinkExtension()])
        self.assertEqual(
            md.convert(text),
            '<p>Some text with a '
            '<a href="http://example.com/WikiLink.html">WikiLink</a>.</p>'
        )

        # MetaData should not carry over to next document:
        self.assertEqual(
            md.convert("No [[MetaData]] here."),
            '<p>No <a class="wikilink" href="/MetaData/">MetaData</a> '
            'here.</p>'
        )

    def testURLCallback(self):
        """ Test used of a custom URL builder. """

        from markdown.extensions.wikilinks import WikiLinkExtension

        def my_url_builder(label, base, end):
            return '/bar/'

        md = markdown.Markdown(extensions=[WikiLinkExtension(build_url=my_url_builder)])
        self.assertEqual(
            md.convert('[[foo]]'),
            '<p><a class="wikilink" href="/bar/">foo</a></p>'
        )

    def testLinkText(self):
        """Test [[link-text|linked-resource]]"""
        from markdown_gollum.wikilinks import WikiLinkExtension
        md = markdown.Markdown(extensions=[WikiLinkExtension(
            base_url='',
            end_url='',
            html_class=''
        )])
        text = "[[link-text|linked-resource]]"
        html = '<p><a href="linked-resource">link-text</a></p>'
        self.assertEqual(md.convert(text), html)

    def testMoreUnicode(self):
        from markdown_gollum.wikilinks import WikiLinkExtension
        md = markdown.Markdown(extensions=[WikiLinkExtension(
            base_url='',
            end_url='',
            html_class=''
        )])
        text = "[[Вопрос к жителям города или отдыхающим «в теме». Ребенку скоро 14 лет." + \
            "|facebook-1945869095704578]]"
        html = '<p><a href="facebook-1945869095704578">' + \
            'Вопрос к жителям города или отдыхающим «в теме». Ребенку скоро 14 лет.' + \
            '</a></p>'
        self.assertEqual(md.convert(text), html)


if __name__ == '__main__':
    unittest.main()
