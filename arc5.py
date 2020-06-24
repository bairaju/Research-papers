# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:07:56 2019

@author: laksh
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:44:53 2019

@author: laksh
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:17:22 2019

@author: laksh
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:29:42 2019

@author: laksh
"""

import numpy as np
import matplotlib.pyplot as plt
M=int(input("enter no of associative memories"))
m=int(input('enter weight matrix1  no of rows'))
n=int(input('enter weight matrix1 no of  columns'))
x=int(input("enter weight matrix2 no of rows "))
y=int(input("enter weight matrix2 no  of columns"))
p=int(input('enter state matrix  no of rows'))
q=int(input('enter state matrix no of  columns'))
v=int(input('enter state matrix  no of rows'))
w=int(input('enter state matrix no of  columns'))
r=int(input('enter threshold matrix1 no of rows'))
s=int(input('enter threshold matrix1 no of columns'))
t=int(input("enter threshold matrix2 no of rows"))
u=int(input("enter threshold matrix2 no of columns"))
print('enter weight1 elements')
weights1 = [[int(input())for j in range(0,n)]for i in range(0,m)]
print(weights1)
print("enter weight2 elements")
weights2 = [[int(input())for j in range(0,y)]for i in range(0,x)]
print(weights2)
print('enter threshold matrix1')
threshold1 = [[float(input()) for j in range (0,s)] for  i in range(0,r)] 
print(threshold1)
print('enter threshold matrix2')
threshold2 = [[float(input()) for j in range (0,u)] for  i in range(0,t)] 
print(threshold2)
v1 =[]                     
print('enter v(0) elements')
a = [[int(input())for j in range (0,q)] for i in range(0,p)] 
v1.append(a)
print(a)
v2=[]
print('enter v(1) elements')
b = [[int(input())for j in range (0,w)] for i in range(0,v)] 
v2.append(b)
print(b)             
for i in range(0,q):
    v1.append(0)
    v[i+1] = np.sign((np.matmul(weights1,v1[i]))-threshold1)
    z = v[i+1]
    z = np.sign((np.matmul(weights1,z))-threshold1)
    if (z-a).all()==0:
        print ("stable state")
        print("i",i+1)
        print('v[i+1]',v[i+1])
    else:
        print("unstable state")
for j in range(0,q):
    v[i+1] = np.sign((np.matmul(weights2,v2))-threshold2)
    z = v[i+1]
    z = np.sign((np.matmul(weights2,z))-threshold2)
    if (z-b).all()==0:
        print ("stable state")
        print("i",i+1)
        print('v[i+1]',v[i+1])
    else:
        print("unstable state")
    
#s=[]       
#for i in range(len(v)):
    #a=np.sign([(np.matmul(v,weights[i]))-threshold[i]])
    #s[i].append(a)
    #print ("output state[i] matrix",s[i])
	 
s1=np.sign([(np.matmul(weights1,v1))-threshold1])
s2=np.sign([(np.matmul(weights2,v2))-threshold2])
print ("output state matrix1",s1)
print("output state matrix2",s2)
s=[]
s.append(s1)
s.append(s2)
print("stacked matrix",s)



	    
