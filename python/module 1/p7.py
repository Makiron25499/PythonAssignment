# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:30:33 2020

@author: Student
"""


n=input("Enter no:")
s=""
x=list(n)
for i in range(len(x)):
    x[i]=int(x[i])+1
    s=s+str(x[i])

print(int(s))    
    