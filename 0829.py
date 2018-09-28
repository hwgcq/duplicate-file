#/usr/bin/env python
#2018-08-25 16:15 hwg
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
 
def HF1(ffp,block=2**20,Method='MD5'):
    from hashlib import md5 as hf
    import sys
    f=open(ffp,'rb')
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
    return h.hexdigest()

def SF1(ff):
    fst=os.stat(ff)
    mtime = datetime.fromtimestamp(fst.st_mtime)
    str_mtime=mtime.strftime(tfmt)
    S='{:,}'.format(fst.st_size)+'\t'+str_mtime
    #f=open(ff,'rb')
    #data=f.read(16)
    #f.close()
    #S+='\t'+str(data)
    return S

def get_key (dic, value):
    return [k for k, v in dic.items() if v == value]
 
def DelDupF(Dir,minSize=0,Del=True,Stamp=True,extn='.md5'):
    t1=datetime.now()
    print(Dir+'\n')
    dic={}
    N,S=GetDirS(Dir)
    n1,s1=0,0
    n2,s2=0,0
    for root, subdirs, files in os.walk(Dir):
        for file in files:
            ff = os.path.join(root,file)
            n1+=1
            s1+=os.path.getsize(ff)
            if os.path.getsize(ff) < minSize:continue #小文件不处理
            rf=os.path.relpath(ff,Dir)
            #print (rf,end="\t")
            print('|',end='')
            h=HF1(ff)
            if h in dic.keys():
                n2+=1
                s2+=os.path.getsize(ff)
                #print('Proc '+'{:,}'.format(n2)+'...',end=' ')
                print('\n'+ff+'\t'+' %d' % (s1/S*100.0)+'%',end='')
                if Del:os.remove(ff)
                if Stamp:f=open(ff+extn,'w');f.write(dic[h]+'\t'+h);f.close()
            else:
                dic[h]=rf
            #print (rf,end="\t")
            #print(' %d' % (s1/S*100.0)+'%')
    print('\n\n'+Dir)
    print('Total\t' +'{:,}'.format(N) +'file(s)\t'+'{:,}'.format(S) +'Byte(s)')
    print('Duplic\t'+'{:,}'.format(n2)+'file(s)\t'+'{:,}'.format(s2)+'Byte(s)')
    t2=datetime.now()
    print('Elapsed Time: ' + str(t2-t1))
    return dic

def SaveDict(dic,fn):
    f=open(fn,'w')
    for key in dic.keys():
        f.write(key+'\t'+dic[key]+'\n')
    f.close()


import tkinter as tk
from tkinter import filedialog 
if __name__=='__main__':
    root = tk.Tk()
    root.withdraw()
    
    Dir=filedialog.askdirectory()
    dic=DelDupF(Dir,minSize=2**10)
    SaveDict(dic,Dir+'.md5')
