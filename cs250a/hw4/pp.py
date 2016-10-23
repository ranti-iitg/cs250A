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
