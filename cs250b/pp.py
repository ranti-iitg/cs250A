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

'''
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

'''

SlistY=[]
SlistX=[]
RlistX=trX[:200]
RlistY=trY[:200]
SlistX.append(trX[0])
SlistY.append(trY[0])
#testfunction
def test(start,end,testX,testY,SlistX,SlistY):
	error=0
	i=start
	while i <  end:
		if np.argmax(testY[i])!=minDis(testX[i],SlistX,SlistY):
			error=error+1
		i=i+1
	return (error,end-start)
#distance function
def minDis(X,ArrX,ArrY):
	i=0
	mdis=999999
	mdisi=-1
	while i<len(ArrX):
		cdis=sqrt(sum( (a - b)**2 for a, b in zip(ArrX[i], X)))
		if cdis<mdis:
			mdis=cdis
			mdisi=i
		i=i+1
	return np.argmax(ArrY[mdisi])
	
#main algo
print "main algo"
print trY[0]
print np.argmax(trY[0])
def Onenn(trX,trY):
	i=0
	while i < 600:
		#print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
		#print np.argmax(trY[i])
		if np.argmax(trY[i])!=minDis(trX[i],SlistX,SlistY):
		#	print "expected"
		#	print i
		#	print trY[i]
		#	print np.argmax(trY[i])
		#	print "but getting"
		#	print  minDis(trX[i],SlistX,SlistY)
			SlistX.append(trX[i])
			SlistY.append(trY[i])
		i=i+1

Onenn(trX,trY)
print "hello"
for item in SlistY:
	print np.argmax(item)

print len(SlistX)
print test(0,100,teX,teY,SlistX,SlistY)
print "again"
Onenn(trX,trY)
print len(SlistX)
print test(0,100,teX,teY,SlistX,SlistY)
print "again"
Onenn(trX,trY)
print len(SlistX)
print test(0,100,teX,teY,SlistX,SlistY)



			

