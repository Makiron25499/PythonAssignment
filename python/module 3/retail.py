# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:54:40 2020

@author: Student
"""

n=int(input("Enter no. of items:"))
whole=0
for i in range(0,n):
   while(True):  
    print("Enter price:",i+1)   
    a=int(input())
    if a > 0:
        whole=whole + a
        break
    else:
        pass
retail=whole*0.5
print("Retail:",retail)        
        
