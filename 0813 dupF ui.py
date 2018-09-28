#! /bin/python
#2018-08-13 21:38 hwg
#delete duplicate files

fnext='.md5'
#import sys,os
import tkinter as tk
from tkinter import filedialog
from HashDir import *

root = tk.Tk()
root.withdraw()

path=filedialog.askdirectory()
HashDir(path,path + fnext)
