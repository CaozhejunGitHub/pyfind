# -*- coding:utf-8 -*-


import os



def param_check(pre, suf, name, path):


    
    if ((name != None and pre != None) or (name != None and suf != None)):
        return -1
    return 0


def do_search(path, level, pre, suf, name):

    os.path.isdir()

    return

allFileNum = 0

def printPath(level, path):  
    global allFileNum  
  
    dirList = []  
    
    fileList = []  
   
    files = os.listdir(path)  
    
    dirList.append(str(level))  
    for f in files:  
        if(os.path.isdir(path + '/' + f)):  
            
            if(f[0] == '.'):  
                pass  
            else:  
                
                dirList.append(f)  
        if(os.path.isfile(path + '/' + f)):  
            
            fileList.append(f)  
    
    i_dl = 0  
    for dl in dirList:  
        if(i_dl == 0):  
            i_dl = i_dl + 1  
        else:  
            
            print '-' * (int(dirList[0])), dl  
            
            printPath((int(dirList[0]) + 1), path + '/' + dl)  
    for fl in fileList:  
        
        print '-' * (int(dirList[0])), fl  
        
        allFileNum = allFileNum + 1  
        
        
