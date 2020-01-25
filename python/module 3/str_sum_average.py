# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:52:46 2020

@author: Student
"""

st=input("Enter string:")
x=st.split(" ")
count,sum,i=0,0,0
while (i<=len(x)):
    try:
      sum=sum+int(x[i])
      i=i+1  
      count=count+1
    except:
      i=i+1
print("sum=",sum,"average=",sum/count)
 