#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
python useful tool collection
'''

def openAnything(source):
    '''
    source: http/ftp | native file | string 
    return a file-like object with read()
    '''
    # try to open with urllib (if source is http, ftp, or file URL)
    import urllib2                        
    try:                                  
        return urllib2.urlopen(source)
    except (IOError, OSError):            
        pass                              

    # try to open with native open function (if source is pathname)
    try:            
        return open(source)
    except (IOError, OSError):
        pass                              

    # treat source as string
    import StringIO        
    return StringIO.StringIO(str(source))

global b
b = True
def to(f):
    f = False
to(b)
print b

def to1():
    b = False

to1()
print b

def to2():
    global b
    b = False

to2()
print b
