import numpy as np

orig_data=np.loadtxt("enorig32.dat",delimiter=" ")
blocked_data=np.loadtxt("enblock32.dat",delimiter=" ")
mapping=[]

count=0

swee=orig_data.shape[0]
for i in range(swee):
  for j in range(swee):
    if (np.abs(orig_data[i,2]-blocked_data[j,2]) < 0.0008):
      print(orig_data[i,0],blocked_data[j,0],orig_data[i,2],blocked_data[j,2])
      mapping.extend((orig_data[i,0],blocked_data[j,0],orig_data[i,2],blocked_data[j,2]))
      count=count+1


