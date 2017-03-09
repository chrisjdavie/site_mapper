'''
Created on 5 Mar 2017

@author: chrisd
'''
import unittest

from ..process_link import is_valid_link, build_link, \
        _relative_url_to_absolute, relative_urls_to_absolute


class TestIsValidLink(unittest.TestCase):


    def test_valid(self):

        test_link = "http://chrisjdavie.github.io/asset.html"

        domain = "http://chrisjdavie.github.io/"

        self.assertTrue(is_valid_link(test_link, domain))


    def test_relative(self):

        test_link = "asset.html"

        domain = "http://chrisjdavie.github.io/"

        self.assertTrue(is_valid_link(test_link, domain))


    def test_different_domain(self):

        test_link = "http://www.google.com/asset.html"

        domain = "http://chrisjdavie.github.io/"

        self.assertFalse(is_valid_link(test_link, domain))


    def test_different_scheme(self):

        test_link = "https://chrisjdavie.github.io/asset.html"

        domain = "http://chrisjdavie.github.io/"

        self.assertFalse(is_valid_link(test_link, domain))


class TestBuildLink(unittest.TestCase):

    def test_absolute_link(self):

        test_link = "http://chrisjdavie.github.io/asset.html"
        domain = "http://chrisjdavie.github.io/"

        merged_url = build_link(test_link, domain)

        self.assertEqual(test_link, merged_url)


    def test_relative_link(self):

        test_rel = "asset.html"
        domain = "http://chrisjdavie.github.io/"
        test_link = "http://chrisjdavie.github.io/asset.html"

        merged_url = build_link(test_rel, domain)

        self.assertEqual(test_link, merged_url)


class Test_relativeUrlToAbsolute(unittest.TestCase):

    def test_relative_link(self):

        test_rel = "asset.html"
        domain = "http://chrisjdavie.github.io/"
        test_link = "http://chrisjdavie.github.io/asset.html"

        merged_url = _relative_url_to_absolute(test_rel, domain)

        self.assertEqual(test_link, merged_url)


    def test_absolute_link(self):

        test_link = "http://google.com/asset.html"
        domain = "http://chrisjdavie.github.io/"

        merged_url = _relative_url_to_absolute(test_link, domain)

        self.assertEqual(test_link, merged_url)


class TestRelativesUrlToAbsolute(unittest.TestCase):

    def test_functionality(self):
        # an integration test, other functionality tested in the relavent
        # modules

        domain = "http://chrisjdavie.github.io/"
        relative_urls = set(["http://google.com/asset.html",
                             "asset.html"])
        target_urls = set(["http://google.com/asset.html",
                           "http://chrisjdavie.github.io/asset.html"])

        gen_urls = relative_urls_to_absolute(relative_urls, domain)

        self.assertSequenceEqual(target_urls,
                                 gen_urls)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
