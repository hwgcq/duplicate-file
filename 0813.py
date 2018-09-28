#/usr/bin/env python
#Guoyabin
#https://www.cnblogs.com/guoyabin/p/6879503.html
#python对文件夹内文件去重
#-*- coding:utf-8 -*-
import os,hashlib
 
def filecount():
    filecount=int(os.popen('dir /B |find /V /C ""').read())
    return(filecount)
 
def md5sum(filename):
    f=open(filename, 'rb')
    md5=hashlib.md5()
    while True:
        fb = f.read(8096)
        if not fb:
            break
        md5.update(fb)
    f.close()
    return (md5.hexdigest())
 
def delfile():
    all_md5={}
    filedir=os.walk(os.getcwd())
    for i in filedir:
        for tlie in i[2]:
            if md5sum(tlie) in all_md5.values():
                os.remove(tlie)
            else:
                all_md5[tlie]=md5sum(tlie)
 
if __name__=='__main__':
    keyword=input('\n请把本程序放到要去重的文件夹内,并按回车继续\n\n')
    oldf=filecount()
    print('去重前有',oldf,'个文件\n\n\n请稍等正在为您删除重复文件...')
    delfile()
    print('\n\n去重后剩',filecount(),'个文件')
    print('\n\n一共帮您删除了',oldf-filecount(),'个文件\n\n')
    keyword=input('请按回车退出')
