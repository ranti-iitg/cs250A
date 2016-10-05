from __future__ import division

import operator

import string



with open("hw1_word_counts_05.txt", "r") as lines:

    wordcount = {}

    total_words = 0

    for line in lines:

        words = [word for word in line.split()]

        wordcount[words[0]]=int(words[1]);

        total_words=total_words+int(words[1]);

    print total_words

    sorted_value = sorted(wordcount.items(), key=operator.itemgetter(1)) 

    print sorted_value[0]

    print len(sorted_value)

    

    print sorted_value[len(sorted_value)-1]


    

    ep = dict()

#ep[0]="D"

   # ep[1]="H"

   # ep[2]="R"

#   ep[3]="I"

    ea = ""

    

    def p_word(str):

	if str in wordcount:

		return wordcount[str]/total_words

	else:

		return 0

		

    def p_evidence_given_word(str):

    	#print str

    	for i in range(5):

    		if i in ep:

    			if str[i]!=ep[i]:

    				return 0

    		else:

    			for itt in ep.items():

    				if itt[1] ==str[i]:

    					return 0

    			for letter in ea:

    				if str[i]==letter:

    					return 0	

   	return 1

    

    

    

    def p_evidence():

    	p_e=0

    	for item in wordcount.items():

    		p_e=p_e + p_word(item[0])*p_evidence_given_word(item[0])

    	return p_e

    

    def p_word_given_evidence(str):

    	return (p_evidence_given_word(str)*p_word(str))/(p_evidence())

    	

    def p_l_in_word(str,l):

    	for i in range(5):

    		if i in ep:

    			jj=0

    		else:

    			if str[i] == l:

    				return  1

    	return 0

    	

    def p_l_given_evidence(l):

    	p_l_e=0

    	for item in wordcount.items():

    		p_l_e=p_l_e+p_word_given_evidence(item[0])*p_l_in_word(item[0],l)

    	return p_l_e



    def p_l_given_evidence_all_alphabets():

        s=string.ascii_uppercase

        for c in s:

            print c

            print p_l_given_evidence(c)

    print "hix	"

    print p_l_given_evidence("E");

    print p_l_given_evidence_all_alphabets();
