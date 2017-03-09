'''
Created on 6 Mar 2017

@author: chrisd
'''

def clean_assets(assets):

    clean = set()

    for asset in assets:
        clean_asset = asset
        clean_asset = clean_asset.replace("'", "")
        clean_asset = clean_asset.split("#")[0]
        clean_asset = clean_asset.replace("\\", "")

        # asset needs content
        if clean_asset:
            clean.add(clean_asset)

    return clean
