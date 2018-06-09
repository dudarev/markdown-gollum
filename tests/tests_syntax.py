"""
This is a single test similar to syntax tests in Python-Markdown that are described at

https://python-markdown.github.io/test_suite/#markdown-syntax-tests

It compares conversions of `./wikilinks.md` with `./wikilinks.html`.
"""

import os
import unittest

import markdown

from markdown_gollum import wikilinks

TEST_IN = 'wikilinks.txt'
TEST_OUT = 'wikilinks.html'


class TestWikiLinks(unittest.TestCase):
    """ Test Wikilinks Extension. """

    def setUp(self):
        self.md = markdown.Markdown(extensions=[wikilinks.WikiLinkExtension()])

    def testSyntax(self):
        """ Test [[wikilinks]]. """
        FILE_DIR = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(FILE_DIR, TEST_IN)) as f_in:
            text_in = f_in.read()
        with open(os.path.join(FILE_DIR, TEST_OUT)) as f_out:
            text_out_expected = f_out.read().strip()
        text_out = self.md.convert(text_in)
        self.assertEqual(
            text_out,
            text_out_expected
        )


if __name__ == '__main__':
    unittest.main()
