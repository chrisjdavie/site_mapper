'''
Created on 5 Mar 2017

@author: chrisd
'''
from html.parser import HTMLParser

TAG_ATTR_ASSETS = { 'a': [ 'href' ], 'link': ['rel'], 'img': ['src'],
                    'script': ['src'] }

class LinkAndAttrHTMLParser(HTMLParser):
    """Parses html - Puts links on the link queue, gets the assets as
    defined by TAG_ATTR_ASSETS"""

    def __init__(self, link_queue):

        self.link_queue = link_queue
        self.assets = set()
        super().__init__()


    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if tag == "a" and attr[0] == "href":
                self.link_queue.put(attr[1].split("#")[0])

            if (tag in TAG_ATTR_ASSETS
                and attr[0] in TAG_ATTR_ASSETS[tag]):
                self.assets.add(attr[1])


    def get_assets_from_feed(self, data):

        self.feed(data)
        assets = self.assets
        self.assets = set()

        return assets

