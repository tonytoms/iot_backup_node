import os as os
import shutil as shutil

'''
Created on Sep 9, 2018

@author: Default
'''

def createOrReplace(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir(path)
        
def checkExistOrCreate(path):
    if os.path.isdir(path):
        return True
    else:
        os.mkdir(path)
        return True
def cutPasteFile(source,dest):
    shutil.copyfile(source, dest)
    os.remove(dest) 
        