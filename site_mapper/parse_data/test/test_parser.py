'''
Created on 5 Mar 2017

@author: chrisd
'''
import queue
import unittest

from ..parser import LinkAndAttrHTMLParser


class TestParser(unittest.TestCase):

    def test_initialisation(self):

        a_queue = "foo"

        a_parser = LinkAndAttrHTMLParser(a_queue)

        self.assertIs(a_queue, a_parser.link_queue)
        self.assertEqual(len(a_parser.assets),
                         0)
        self.assertIsInstance(a_parser.assets,
                              set)


    def test_link_html_added_to_queue(self):

        link = "main.html"

        link_html = "<p><a class=link href=" + link + ">tag soup</p ></a>"

        a_queue = queue.Queue()

        a_parser = LinkAndAttrHTMLParser(a_queue)
        a_parser.feed(link_html)

        parsed_link = a_queue.get_nowait()

        self.assertEqual(link,
                         parsed_link)


    def test_link_text_after_hash_removed(self):

        link = "main.html"
        hash_link = "#1234"

        link_html = "<p><a class=link href=" \
                    + link + hash_link \
                    + ">tag soup</p ></a>"

        a_queue = queue.Queue()

        a_parser = LinkAndAttrHTMLParser(a_queue)
        a_parser.feed(link_html)

        parsed_link = a_queue.get_nowait()

        self.assertEqual(link,
                         parsed_link)


    def test_attrs_from_feed(self):

        link = "main.html"

        link_html = "<p><a class=link href=" + link + ">tag soup</p ></a>"

        a_queue = queue.Queue()

        a_parser = LinkAndAttrHTMLParser(a_queue)
        a_parser.feed(link_html)

        self.assertIn(link, a_parser.assets)


    def test_get_assets_from_feed(self):

        link = "main.html"

        link_html = "<p><a class=link href=" + link + ">tag soup</p ></a>"

        a_queue = queue.Queue()

        a_parser = LinkAndAttrHTMLParser(a_queue)
        assets = a_parser.get_assets_from_feed(link_html)

        self.assertIn(link, assets)
        self.assertEqual(len(a_parser.assets), 0)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
