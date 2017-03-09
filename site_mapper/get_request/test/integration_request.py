'''
Testing connection to the outside world

Created on 5 Mar 2017

@author: chrisd
'''
import datetime
import unittest

from ..request import request, RequestError

class TestRequest(unittest.TestCase):


    def test_gets_data(self):
        # testing connection to a yoyo wallet returns something

        test_url = "http://chrisjdavie.github.io"

        data, _ = request(test_url)

        self.assertGreater(len(data), 0)


    def test_gets_content_type(self):
        # testing connection to a yoyo wallet returns html data

        test_url = "http://chrisjdavie.github.io"

        _, content_type = request(test_url)

        self.assertSequenceEqual('text/html; charset=utf-8',
                                 content_type)



    def test_raises(self):
        test_url = "http://chrisjdavie.github.io/hopefully_not_valid"

        self.assertRaises(RequestError,
                          request,
                          test_url)


    def test_timeout(self):
        test_url = "http://chrisjdavie.github.io/hopefully_not_valid"

        start_time = datetime.datetime.now()

        self.assertRaises(RequestError,
                          request,
                          test_url)

        dt = datetime.datetime.now() - start_time

        self.assertGreaterEqual(dt.total_seconds(), 3)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
