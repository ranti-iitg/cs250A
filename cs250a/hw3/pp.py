import random
import math 
import matplotlib.pyplot as plt
import numpy as np

List2D=[]

def make_sample(n):
	for x in range(n):
		list=[]
		for k in range(10):
			coin = random.randint(0, 1)
			list.append(coin)
		
		List2D.append(list)


def make_sample_append(List2D):
		list=[]
		for k in range(10):
			coin = random.randint(0, 1)
			list.append(coin)
		List2D.append(list)
		 
def count_i(List2D):
	count=0
	for x in List2D:
		if x[i]==1:
			count = count +1
	
	return count


def list_to_int(list1d):
	ret=0
	two=1
	for x in list1d:
		if x ==1:
			ret=ret+two
		
		two=two*2

	return ret

def probz_list1d(list1d):
	ll=list_to_int(list1d)
	return (2.0/3.0)*math.pow((0.2),abs(ll-128))

def denominator(list2d):
	sums=0
	for x in list2d:
		sums=sums+probz_list1d(x)
	return sums
def numerator(list2d,ii):
	sums=0
	for x in list2d:
		if x[ii]==1:
			sums=sums+probz_list1d(x)
	return sums


def final(n,ii):
	make_sample_append(List2D)
	#print List2D
	num=numerator(List2D,ii)/denominator(List2D)
	#del List2D[:]
	#print "Check"
	#print List2D
	#print "Check close"
	return num


list11=[1,0]
print list_to_int(list11)


i=1
listx=[]
listy=[]
while i<100000000:
	if i%10000==0:
		#print i
		listx.append(i/10000)
		temp=final(i,9)
		listy.append(temp)
		#print temp
		
	i=i+1

x=np.array(listx)
y=np.array(listy)
plt.plot(x, y)
plt.show()
