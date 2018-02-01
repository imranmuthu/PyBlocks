from user import *

def newUser(name):
    new = user(name)
    new.set_name(name)
    new.set_uniqueAddr(name)
    print(new.uniqueAddr)

def main():
    newUser("hello")