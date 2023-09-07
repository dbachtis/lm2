import numpy as np,pandas as pd
np.printoptions(precision=6, suppress=True)
import sys
L=int(sys.argv[1])
betas=[float(sys.argv[2])]
sweeps=[int(sys.argv[3])]
b1=float(sys.argv[4])
b2=float(sys.argv[5])
step=float(sys.argv[6])
fname=str(sys.argv[7])
fname2=str(sys.argv[8])
simulations=len(betas)

energies=np.empty((0,))
magnetizations=np.empty((0,))
for beta in betas:
  t=np.loadtxt(fname,delimiter=" ")
  energies=np.append(energies,t[:,0])
  magnetizations=np.append(magnetizations,t[:,1])
energies=np.reshape(energies,(len(energies),1))
magnetizations=np.reshape(magnetizations,(len(magnetizations),1))
menergy=np.mean(energies)


energiesr=np.empty((0,))
magnetizationsr=np.empty((0,))
for beta in betas:
  t=np.loadtxt(fname2,delimiter=" ")
  energiesr=np.append(energiesr,t[:,0])
  magnetizationsr=np.append(magnetizationsr,t[:,1])
energiesr=np.reshape(energiesr,(len(energiesr),1))
magnetizationsr=np.reshape(magnetizationsr,(len(magnetizationsr),1))

N=L*L

for beta in np.arange(b1,b2,step):

  sum1=energiesr*np.exp(-(beta-betas[0])*(energies-menergy))
  sum2=np.exp(-(beta-betas[0])*(energies-menergy))
  sum3=np.abs(magnetizationsr)*np.exp(-(beta-betas[0])*(energies-menergy))

  en=np.sum(sum1)/np.sum(sum2)
  m=np.sum(sum3)/np.sum(sum2)

  en=en/N
  m=m/N

  
  

  print( np.round(beta,5),en,m)

