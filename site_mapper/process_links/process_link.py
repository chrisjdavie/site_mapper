'''
Created on 5 Mar 2017

@author: chrisd
'''
from urllib.parse import urlparse, urljoin

def is_valid_link(url, domain):
    """Tests if the url should be explored - either a relative url
    or an absolute url within the domain"""

    is_valid = False

    o_domain = urlparse(domain)
    o_url = urlparse(url)

    if not o_url.scheme and not o_url.netloc:
        # relative link
        is_valid = True
    else:
        # absolute link
        if o_url.scheme == o_domain.scheme:
            if o_url.netloc == o_domain.netloc:
                is_valid = True

    return is_valid


def build_link(url, domain):

    path = urlparse(url).path
    return urljoin(domain, path)


def relative_urls_to_absolute(urls, domain):
    """converts a set of relative and absolute urls to absolute urls
    within domain"""

    full_urls = set()

    for url in urls:
        full_urls.add(_relative_url_to_absolute(url, domain))

    return full_urls


def _relative_url_to_absolute(url, domain):
    """converts a relative to an absolute urls within domain,
    returns absolute urls unchanged"""

    o_url = urlparse(url)
    full_url = url

    if not o_url.scheme and not o_url.netloc:
        # relative link
        full_url = build_link(url, domain)

    return full_url
