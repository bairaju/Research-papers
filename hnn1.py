import numpy as np
import matplotlib.pyplot as plt

weights = np.matrix([[0,1,1],
                    [1,0,1],
                    [1,1,0]])

threshold = np.matrix([[0.2, 0.2, 0.2],
                       [0.2, 0.2, 0.2],
                       [0.2, 0.2, 0.2]])
v =[]                     
a= np.matrix([[-1, 1, 1],
              [1, -1, 1],
              [1, 1, -1]])
v.append(a)
               
for i in range(0,3):
    v.append(0)
    v[i+1] = np.ceil((np.matmul(weights,v[i]))-threshold)
    print(v[i+1])  
    z = v[i+1]
    z = np.ceil((np.matmul(weights,z))-threshold)
    if ((z-a).all()==0):
	    print("z_matrix",z)
	    print('v[i+1]',v[i+1])
	    print("stable_state")
	    