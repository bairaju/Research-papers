import numpy as np
import matplotlib.pyplot as plt
m=int(input('enter weight matrix  no of rows'))
n=int(input('enter weight matrix no of  columns'))
p=int(input('enter state matrix  no of rows'))
q=int(input('enter state matrix no of  columns'))
r=int(input('enter threshold matrix no of rows'))
s=int(input('enter threshold matrix no of columns'))
print('enter weight elements')
weights = [[int(input()) for x in range (m)] for y in range(n)] 
print(weights)
#weights = np.matrix([[0,1],
#                    [1,0]])

print('enter threshold matrix')
threshold = [[float(input()) for x in range (p)] for y in range(q)] 
print(threshold)

#threshold = np.matrix([[0.3, 0.1],
#                       [0.1, 0.2]])

v =[]                     
#a= np.matrix([[4, 1],[2, 3]])
print('enter v(0) elements')
a = [[float(input()) for x in range (r)] for y in range(s)] 
v.append(a)
print(a)
b= np.matrix([[0,0],[0,0]])                 
for i in range(0,4):
    v.append(0)
    v[i+1] = np.ceil((np.matmul(weights,v[i]))-threshold)
    #v[i+1] = np.sign((np.matmul(weights,v[i]))-threshold)
    z = v[i+1]
    z = np.ceil((np.matmul(weights,z))-threshold)
    #z = np.sign((np.matmul(weights,z))-threshold)
    if ((z-a).any() ==b.any()):
	    print("z_matrix",z)
	    print("i",i+1)
	    print('v[i+1]',v[i+1])
	    print("stable_state")
	    