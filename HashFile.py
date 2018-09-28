#! /bin/python
#2018-08-13 22:11 hwg

def HashFile(filefullpath,block=2**20):
    from hashlib import md5 as hf
    import sys
    f=open(filefullpath,'rb')
    m=hf()
    i=0
    while True:
        i+=1
        if i>=10:
            sys.stdout.write('.')
            i=0
        data=f.read(block)
        if not data:
            break
        m.update(data)
    f.close()
    return m
