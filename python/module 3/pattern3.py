# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:18:38 2020

@author: Student
"""

c=int(input("Enter no. of rows:" ))
for i in range(0,c):
 if i==int(c/2):
  print(" ",end=" ")   
  for i in range(0,c): 
   print("*",end=" ")
   if i==c-1:
       print()
 else:
   print(" "*c+"*")  

     