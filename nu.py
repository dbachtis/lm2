#A naive calculation of nu. A fit is much better
import numpy as np

data=np.loadtxt("map.dat",delimiter=" ")

beta1=0.4405
beta2=0.4410

for i in range(data.shape[0]):

    if(data[i,1]==beta1):
        beta1prime=data[i,0]

    if(data[i,1]==beta2):
        beta2prime=data[i,0]
        

nu=np.log(2)/np.log((beta2prime-beta1prime)/(beta2-beta1))

print(nu)

