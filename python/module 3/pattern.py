# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:54:43 2020

@author: Student
"""

def m():
 l=[[0]*5]*4   
 for i in range(0,4):
  for j in range(0,5):
      if (i==0 and j==0)  or  (i==1 and j==0)  or (i==2 and j==0) or (i==0 and j==4) or (i==1 and j==4) or (i==2 and j==4) or (i==3 and j==4) or (i==1 and j==1) or (i==1 and j==3) or (i==1 and j==4) or (i==3 and j==4) : 
          l[i][j]="*" 
      else:
        l[i][j]=""  
 for i in range(0,4):
  for j in range(0,5): 
    print(l[i][j],end=" ")  
m()    