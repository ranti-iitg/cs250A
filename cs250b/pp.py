from load import mnist
import numpy as np
from math import sqrt

S=[]

#load data
trX, teX, trY, teY = mnist(onehot=True)
print trX.shape
print trX[0]
print trY.shape
print trY[0]

#S.append(np.array([1,0,3]))
#S[0]=np.vstack([S[0],np.array([2,0,3])])
#print S[0]


i=0
while i<10:
	j=0
	while j<600:
		j=j+1
		if np.argmax(trY[j])==i:
			S.append(trX[j])
			i=i+1
			break


print S
print "hello"
print S[0]


SlistY=[]
SlistX=[]
SlistX.append(trX[0])
SlistY.append(trY[0])

def minDis(X,ArrX,ArrY):
	i=0
	mdis=0
	mdisi=-1
	while i<len(ArrX):
		cdis=sqrt(sum( (a - b)**2 for a, b in zip(ArrX[i], X)))
		if cdis<mdis:
			mdis=cdis
			mdisi=i
		i=i+1
	return np.argmin(ArrY[mdisi])
	

def Onenn(trX,trY):
	i=0
	while i < 60000:
		if np.argmin(trY[i])!=minDis(trX[i],SlistX,SlistY):
			SlistX.append(trX[i])
			SlistY.append(trY[i])
		i=i+1
Onenn(trX,trY)
print "hello"
print SlistX
			

