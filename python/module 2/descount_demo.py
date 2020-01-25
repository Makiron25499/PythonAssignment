# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:09:47 2020

@author: Student
"""

p=int(input("Enter no. of packages:"))
d=0
ta=p*99
if p>=10:
    d=ta*(10/100)   
elif p>=20:
    d=ta*(20/100)   
elif p>=50:
    d=ta*(30/100)   
elif p>=100 :
    d=ta*(40/100)
ta=ta-d
print("Discount amount:",d)
print("Total amount paid:",ta)    
    
    
