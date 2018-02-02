from basic_crypto import *

class user(object):
    name = " "
    uniqueAddr = " "

    def __init__(self, name, uniqueAddr =None):
        self.name = name
        self.uniqueAddr = uniqueAddr

    def set_name(self, name):
        self.name = name

    def set_uniqueAddr(self, name):
        self.uniqueAddr = name

