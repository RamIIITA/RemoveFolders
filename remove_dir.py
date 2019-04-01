#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:08:04 2019

@author: ram
"""

removed = 0
 
def checkfile(file, name):    
    subfiles = os.listdir(file)    
    
    if name in subfiles:
        return True
    
    for s in subfiles:        
        if os.path.isdir(file+'/'+s):
            return checkfile(file+'/'+s, name)    
    return False
    

import shutil as sh
import os 
path = "/home/ram/Desktop/Thesis/PDB/Output_prosite_pattern"

name = "3D_structure.txt"
files = os.listdir(path)
Total_files = len(files)
os.chdir(path)

for file in files:
    if os.path.isdir(file):
        if not(checkfile(file, name)):
            sh.rmtree(file)
            removed+=1
            
print("successful process completion")
print("Total files before process: ", Total_files)
print("Files removed: ", removed)
print("Remaining Files", Total_files-removed)
            
        