#/usr/bin/env python
#Guoyabin
#https://www.cnblogs.com/guoyabin/p/6879503.html
#hwg
#-*- coding:utf-8 -*-
import os
from datetime import datetime
tfmt='%Y-%m-%d %H:%M:%S'

def GetDirS(dir,maxN=2**20):
    from os.path import join, getsize
    S = 0
    N = 0
    for root, dirs, files in os.walk(dir):
        S += sum([getsize(join(root, name)) for name in files])
        N += len(files)
        if N > maxN:
            print('Too many files(>'+'{:,}'.format(maxN)+')!')
            break
    return N,S
 
def HashFile(filefullpath,block=2**20):
    from hashlib import md5 as hf
    import sys
    f=open(filefullpath,'rb')
    h=hf()
    i=0
    while True:
        i+=1
        if i>=10:
            sys.stdout.write('.')
            i=0
        data=f.read(block)
        if not data:
            break
        h.update(data)
    f.close()
    return h

def get_key (dic, value):
    return [k for k, v in dic.items() if v == value]
 
def DelDupF(Dir):
    print(Dir+'\n')
    dic={}
    N,S=GetDirS(Dir)
    dn,ds=0,0
    i=0
    for root, subdirs, files in os.walk(Dir):
        for file in files:
            ff = os.path.join(root,file)
            dn+=1
            ds+=os.path.getsize(ff)
            rf=os.path.relpath(ff,Dir)
            print (rf,end="\t")
            h=HashFile(ff).hexdigest()
            if h in dic.keys():
                i+=1
                stri='{:,}'.format(i)
                print('Deleting '+stri+'...',end=' ')
                os.remove(ff)
                f=open(ff+'.md5','w')
                f.write(dic[h]+'\t'+h)
                f.close()
            else:
                dic[h]=rf
            print(' %d' % (ds/S*100.0)+'%')
    strN='{:,}'.format(N)
    strS='{:,}'.format(S)
    stri='{:,}'.format(i)
    print ('\nTotal '+strN+'file(s) '+strS+'B,Delete '+stri+'file(s)!')

import tkinter as tk
from tkinter import filedialog 
if __name__=='__main__':
    root = tk.Tk()
    root.withdraw()
    
    Dir=filedialog.askdirectory()
    DelDupF(Dir)
    
