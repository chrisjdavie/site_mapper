'''
Created on 3 Mar 2017

@author: chrisd
'''
import time
import urllib3


class RequestError(BaseException):
    """A request has not been completed successfully"""
    pass

http = urllib3.PoolManager()

def request(url):
    """Simple request handler for a url - on a 200 status, it returns the data,
    otherwise raises a request error
    """

    for _ in range(3):
        # try the url 3 times, with
        r = http.request('GET', url)
        if r.status == 200:
            break
        else:
            time.sleep(1)
    else:
        raise RequestError("http request to " + url + " has failed with "
                           "non-200 response " + str(r.status))
    return str(r.data), r.headers['Content-Type']
