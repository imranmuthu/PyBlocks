from basic_crypto import *

class user(object):
    name = " "
    uniqueAddr = " "

    def __init__(self, name =None, uniqueAddr =None):
        self.name = name
        self.uniqueAddr = uniqueAddr

    def set_name(self, name):
        self.name = name

    def set_uniqueAddr(self, uniqueAddr):
        salt = generate_salt(uniqueAddr)
        self.uniqueAddr = encrypt(derive_key(4096 ,salt), uniqueAddr)

