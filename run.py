'''
Created on 6 Mar 2017

@author: chrisd
'''
import sys

from sitemap_yoyo.run_mapper import run_mapper

if __name__ == '__main__':

    domain = sys.argv[1]

    N_p = 2
    if len(sys.argv) > 2:
        N_p = int(sys.argv[2])

    run_mapper(domain, N_p)
