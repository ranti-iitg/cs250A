import numpy as np
fu = open('unigram.txt', 'r')
xxu = fu.readlines()
listcount=[]
total_words=0
for xu in xxu:
	listcount.append(int(xu))
	total_words=total_words+int(xu)

print listcount[0]
print total_words

listvocab=[]
fv = open('vocab.txt', 'r')
xxv = fv.readlines()
for xv in xxv:
	listvocab.append(xv[:-1])

print listvocab[0]
print listvocab[1]

def p_w(word):
	countw=listcount[0]
	if word in listvocab:
		iw=listvocab.index(word)
		countw=listcount[iw]
	print "hi"
	print countw
	print total_words
	return float(float(countw)/float(total_words))


print p_w("AND")


def print_p_w_a():
	for word,i in zip(listvocab,range(len(listvocab))):
		if word[:1]=="A":
			print word
			print float((float(listcount[i])/float(total_words)))

print_p_w_a()

dd=np.zeros((500,500))

fb = open('bigram.txt', 'r')
xxb = fb.readlines()
for xb in xxb:
	nums = [int(n) for n in xb.split()]
	dd[nums[0]-1][nums[1]-1]=nums[2]

print dd[0][0]

def p_w_w(word_dash,word):
	count_w_dash_w=0
	count_w=0;
	index_word_dash=0
	index_word=0
	if word_dash in listvocab:
		index_word_dash=listvocab.index(word_dash)
	if word in listvocab:
		index_word=listvocab.index(word)
	count_w_dash_w=dd[index_word,index_word_dash]
	count_w=listcount[index_word]
	if(count_w_dash_w==0):
		print "00000000000000000000000000"
		print word_dash
		print word
		print "00000000000000000000000000000000000000000000000"
	return float(float(count_w_dash_w)/float(count_w))

def p_w_given_not_given(word_dash):
	list_all=[]
	for w in listvocab:
		j=p_w_w(word_dash,w)
		list_all.append(j)

	list3=sorted(range(len(list_all)), key=lambda i: list_all[i])[-5:]
#	list_words=listvocab[list3]
	for ii in list3:
		print listvocab[ii]
		print list_all[ii]




p_w_given_not_given("THE")


import math
import sys
def give_it_u(sentence):
	sentence_upper=sentence.upper()
	sentence_upper=sentence_upper[:-1]
	words=sentence_upper.split()
	ret=0;
	for word in words:
		ret=ret+math.log(p_w(word),2)

	return ret


give_it_u("Last week the stock market fell by one hundred points.")

def give_it_b(sentence):
	sentence_upper=sentence.upper()
	sentece_upper=sentence_upper[:-1]
	words=sentence_upper.split()
	ret=0
	for i in range(len(words)):
		if i==0:
			ret=ret+math.log(p_w(words[i]),2)
		else:
			ret=ret+math.log(max(p_w_w(words[i],words[i-1]),sys.float_info.min),2)
	
	return ret

print give_it_b("Last week the stock market fell by one hundred points.")
print give_it_u("The nineteen officials sold fire insurance.")
print give_it_b("The nineteen officials sold fire insurance.")

def give_m_y(y,sentence):
	sentence_upper=sentence.upper()
	sentence_upper=sentence_upper[:-1]
	words=sentence_upper.split()
	ret=0
	for i in range(len(words)):
		if i==0:
			ret=ret+math.log(p_w(words[i]),2)
		else:
			ret=ret+math.log(max(((1-y)*p_w(words[i])+y*p_w_w(words[i],words[i-1])),sys.float_info.min),2)

	return ret


print give_m_y(1,"The nineteen officials sold fire insurance.")	

import matplotlib.pyplot as plt
j=0.01
i=0
listx=[]
listy=[]
while i<=1:
	listy.append(give_m_y(i,"The nineteen officials sold fire insurance."))
	listx.append(i)
	i=i+j

plt.plot(listx,listy)
plt.show()

