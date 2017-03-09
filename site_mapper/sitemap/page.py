'''
Created on 6 Mar 2017

@author: chrisd
'''
from site_mapper.parse_data.clean_assets import clean_assets
from site_mapper.process_links.process_link import relative_urls_to_absolute

class Page(str):
    '''
    Represents a page in the sitemap.

    Inherits from string to reproduce sorting while allowing for
    an assets parameter
    '''

    def __new__(cls, url, assets, domain):
        '''
        '''

        obj = str.__new__(cls, url)
        obj.assets = obj._parse_assets(assets, domain)
        return obj


    def _parse_assets(self, assets, domain):
        parsed_assets = assets
        parsed_assets = clean_assets(parsed_assets)
        parsed_assets = relative_urls_to_absolute(parsed_assets,
                                                  domain)
        sorted_assets = list(parsed_assets)
        sorted_assets.sort()
        return sorted_assets
