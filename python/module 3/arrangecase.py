# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:33:41 2020

@author: Student
"""

s=input("Enter string:")
st,sr="",""
for i in range(len(s)):
    if s[i].islower():sr=sr+s[i]
    if s[i].isupper():st=st+s[i]
print(sr+st)        
        