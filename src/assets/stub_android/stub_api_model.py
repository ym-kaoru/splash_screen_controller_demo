# -*- coding: utf-8 -*-
import os
import sys


class ApiModel(object):

    def __init__(self, api_call_limit):
        super(ApiModel, self).__init__()
        self.api_call_limit = api_call_limit
        self.delegates = {}
        self.responseAvailable = False
        self.apiRequested = False
        self.apiRequestCounter = 0

    def connect(self, delegate):
        if delegate in self.delegates:
            raise RuntimeError("Already connected")

        self.delegates[delegate] = delegate

    def disconnect(self, delegate):
        del self.delegates[delegate]

    def dispatchEvent(self):
        if not self.apiRequested:
            raise RuntimeError("requestApi required")

        self.responseAvailable = True
        for delegate in self.delegates.iterkeys():
            delegate.receiveResponse()

    def isResponseAvailable(self):
        return self.responseAvailable

    def requestApi(self):
        self.apiRequested = True
        self.apiRequestCounter += 1
        print "  * requestApi %d" % self.apiRequestCounter

        if self.api_call_limit > 0 and self.api_call_limit < self.apiRequestCounter:
            raise RuntimeError("Api call limit exceeded. (limit=%d)" % self.api_call_limit)
