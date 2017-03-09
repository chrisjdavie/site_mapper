'''
Created on 6 Mar 2017

@author: chrisd
'''
import unittest

from ..page import Page

class TestPage(unittest.TestCase):

    def test_initialises(self):

        url = "foo"
        assets = set([ "bar" ])

        a_page = Page(url, assets, "")

        self.assertEqual(url,
                         a_page)
        self.assertSequenceEqual(list(assets),
                         a_page.assets)


    def test_assets_sorts(self):

        url = "foo"
        assets = [ "b", "a" ]

        a_page = Page(url, assets, "")

        self.assertEqual(url,
                         a_page)
        self.assertNotEqual(assets,
                            a_page.assets)
        self.assertSequenceEqual(sorted(assets),
                                 a_page.assets)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
