# -*- coding: utf-8 -*-
'''
Created on 5 Mar 2017

@author: chrisd
'''
import multiprocessing as mp
from site_mapper.get_request.request import request, RequestError
from site_mapper.parse_data.parser import LinkAndAttrHTMLParser
from site_mapper.process_links.process_link import is_valid_link, build_link
from site_mapper.sitemap.page import Page


def request_worker(full_url, data_queue):

    try:
        data, content_type = request(full_url)
        data_queue.put((data, content_type, full_url))

    except RequestError:
        pass


def run_mapper(domain, N_p):

    # initialise variables
    pool = mp.Pool(processes=N_p - 1)

    link_queue = mp.Queue()
    mngr = mp.Manager()
    data_queue = mngr.Queue()

    visited_urls = set()
    parser = LinkAndAttrHTMLParser(link_queue)

    link_queue.put("")

    site_pages = []

    processes = []

    # starting loop

    should_run = True

    while should_run:

        # request data from all the available urls
        while not link_queue.empty():
            url = link_queue.get()

            if is_valid_link(url, domain):
                full_url = build_link(url, domain)
                if full_url not in visited_urls:

                    visited_urls.add(full_url)
                    p = pool.apply_async(request_worker,
                                         args=(full_url,
                                               data_queue))
                    processes.append(p)

        # process the data from the requests
        while not data_queue.empty():

            data, content_type, full_url = data_queue.get()

            if 'html' in content_type:
                assets = parser.get_assets_from_feed(data)
                url = full_url.replace(domain, "")
                site_pages.append(Page("/" + url,
                                       assets,
                                       domain))

        # test if the parallel processing should continue
        if link_queue.empty() and data_queue.empty():

            ii_del = []
            for i, p in enumerate(processes):
                if p.ready():
                    p.get()
                    ii_del.append(i)

            for i in ii_del[::-1]:
                processes.pop(i)

            if (link_queue.empty() and data_queue.empty()
                and not processes):
                should_run = False

    # print the results
    site_pages.sort()
    print(u'\033[1m' + 'Sitemap' + u'\033[0m')
    print()
    for a_page in site_pages:
        print(u"\t• " + a_page)

    for a_page in site_pages:
        print()
        print()
        print(u'\033[1m' + 'Assets on ' + a_page + u'\033[0m')
        print(u"\t• <a href=\"*\" />, <link rel=\"*\" />, <img src=\"*\" />,"
              " <script src=\"*\" />")
        for asset in a_page.assets:
            print("\t\t◦ " + asset)
