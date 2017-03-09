'''
Created on 9 Mar 2017

@author: chrisd
'''
from multiprocessing import JoinableQueue
from multiprocessing import Process

class Requester(object):

    def __init__(self, num_workers=2):
        self.queue = JoinableQueue()
        self.processes = [Process(target=self.request)
                            for _ in range(num_workers)]

    def add_url(self, url):
        self.queue.put(url)


    def request(self):
        url = self.queue.get()
        while url is not None:

            # TODO - actually send a request here

            self.queue.task_done()

            url = self.queue.get()


    def terminate(self):

        # send the terminate command
        for _ in self.processes:
            self.queue.put(None)

        # wait for processing to finish
        for p in self.processes:
            p.join()

# TODO:

# add the requester code
# figure out how to unit test this
# employ it in the main chunk of the code
