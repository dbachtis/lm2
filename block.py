import numpy as np
#boundary conditions are helical

def majority_rule(x):
  if(x<0):
    return -1
  elif(x>0):
    return  1
  else:
    return np.random.choice([-1, 1])

L=64
beta=0.440687
data=np.loadtxt("L"+str(L)+"b"+str(beta)+".csv")

#First apply the renormalization group transformation
blo=int(L*L/4)
spinblocked=np.empty((0,blo))
for row in data:
  blocked=[]
  i=0
  while i < (L*L-L):  
    if((i+2) % (L) == 0):
      count=row[i]+row[i+1]+row[i+L]+row[i+L+1]
      blocked.append(majority_rule(count))
      i=i+L+2
      continue
    count=row[i]+row[i+1]+row[i+L]+row[i+L+1]
    blocked.append(majority_rule(count))
    i=i+2
  blocked=np.reshape(blocked,(1,blo)) 
  spinblocked= np.append(spinblocked,blocked,axis=0)


  
L2=int(L/2)
#Calculate the internal energy and magnetization of the original L=64 system
dx=np.roll(np.copy(data),-1,axis=1)
dy=np.roll(np.copy(data),-L,axis=1)
energies=-np.sum(data*(dx+dy),axis=1)
magnetizations=np.sum(data,axis=1)
energies=np.reshape(energies,(len(energies),1))
magnetizations=np.reshape(magnetizations,(len(magnetizations),1))
np.savetxt('origL'+str(L)+'b'+str(beta)+'.dat', np.c_[energies,magnetizations])

#Calculate the internal energy and magnetization of the renormalized L'=32 system
dx=np.roll(np.copy(spinblocked),-1,axis=1)
dy=np.roll(np.copy(spinblocked),-L2,axis=1)
energies_blocked=-np.sum(spinblocked*(dx+dy),axis=1)
magnetizations_blocked=np.sum(spinblocked,axis=1)
energies_blocked=np.reshape(energies_blocked,(len(energies_blocked),1))
magnetizations_blocked=np.reshape(magnetizations_blocked,(len(magnetizations_blocked),1))
np.savetxt('blockL'+str(L2)+'b'+str(beta)+'.dat', np.c_[energies_blocked,magnetizations_blocked])

#Calculate the internal energy and magnetization of the original L=32 system
data32=np.loadtxt("L"+str(L2)+"b"+str(beta)+".csv")
dx=np.roll(np.copy(data32),-1,axis=1)
dy=np.roll(np.copy(data32),-L2,axis=1)
energies=-np.sum(data32*(dx+dy),axis=1)
magnetizations=np.sum(data32,axis=1)
energies=np.reshape(energies,(len(energies),1))
magnetizations=np.reshape(magnetizations,(len(magnetizations),1))
np.savetxt('origL'+str(L2)+'b'+str(beta)+'.dat', np.c_[energies,magnetizations])
