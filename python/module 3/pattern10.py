# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:21:06 2020

@author: Student
"""
c=int(input("Enter no. of rows:" ))
for i in range(c,0,-1):
  if i!=1:
    print("*"*i)
  else:
    print("*",end=" ")  
for i in range(0,c+1):     
  print("*"*i)
  
 
     
  
  