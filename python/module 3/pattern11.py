# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:32:35 2020

@author: Student
"""

c=int(input("Enter no. of rows:" ))
for i in range(1,c+1):
  print(" "*(c-i),"*"*(i*2-1))
for i in range(c-1,0,-1):
  print(" "*(c-i),"*"*(i*2-1))  