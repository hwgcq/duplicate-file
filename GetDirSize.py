#! /bin/python
#2018-08-13 22:11 hwg

def GetDirSize(dir):
    import os
    from os.path import join, getsize
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size
