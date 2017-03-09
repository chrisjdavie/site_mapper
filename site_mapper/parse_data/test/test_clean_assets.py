'''
Created on 6 Mar 2017

@author: chrisd
'''
import unittest

from ..clean_assets import clean_assets

class TestCleanAssets(unittest.TestCase):


    def test_remove_single_quotes(self):
        with_quote = "'assets/js/sss.min.js'"
        wo_quote = "assets/js/sss.min.js"

        assets = set(["'assets/js/sss.min.js'"])

        clean = clean_assets(assets)

        self.assertIn(wo_quote, clean)
        self.assertNotIn(with_quote, clean)


    def test_split_on_hash(self):
        asset_wo_hash = 'foo'
        asset_w_hash = asset_wo_hash + '#bar'

        assets = set([asset_w_hash])

        clean = clean_assets(assets)

        self.assertIn(asset_wo_hash, clean)
        self.assertNotIn(asset_w_hash, clean)


    def test_skip_leading_hash(self):

        asset_w_hash = '#bar'

        assets = set([asset_w_hash])

        clean = clean_assets(assets)

        # set should be empty now
        self.assertEqual(len(clean),
                         0)


    def test_clean_backslashes(self):
        asset_w_bs = r'\foo\\'
        asset_wo_bs = 'foo'

        assets = set([asset_w_bs])

        clean = clean_assets(assets)

        self.assertIn(asset_wo_bs, clean)
        self.assertNotIn(asset_w_bs, clean)





if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
