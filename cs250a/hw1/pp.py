from __future__ import division
import operator


with open("hw1_word_counts_05.txt", "r") as lines:
    wordcount = {}
    total_words = 0
    for line in lines:
        words = [word for word in line.split()]
     #   print(words)
      #  print words[0]
        wordcount[words[0]]=int(words[1]);
        total_words=total_words+int(words[1]);
    print total_words
    sorted_value = sorted(wordcount.items(), key=operator.itemgetter(1)) 
    print sorted_value[0]
  #  print sorted_value[1]
   # print sorted_value[3]
    #print sorted_value[4]
    #print sorted_value[5]
    
    print len(sorted_value)
    
    print sorted_value[len(sorted_value)-1]
   # print sorted_value[len(sorted_value)-2]
   # print sorted_value[len(sorted_value)-3]
   # print sorted_value[len(sorted_value)-4]
   # print sorted_value[len(sorted_value)-5]
    
    ep = dict()
    ep[0]="D"
   # ep[1]="H"
   # ep[2]="R"
    ep[3]="I"
    ea = "A"
   # for it in ep.items():
    #	print it
    #for it in ea:
    #	print it
    
    def p_word(str):
        #print "ddddddddd"
        #print str
        #print "eeeeeee"
	if str in wordcount:
		#print "sssssssssssssssssssss"
		#print wordcount[str]
		#print total_words
		#print "tttttttttt"
		return wordcount[str]/total_words
	else:
		return 0
		
    def p_evidence_given_word(str):
    	#print str
    	for i in range(5):
    		if i in ep:
    			#print "yyyyyyyyyyyyy"
    			#print i
    			if str[i]!=ep[i]:
    				return 0
    		else:
    			for itt in ep.items():
    				if itt[1] ==str[i]:
    					#print "tttttttttttttttttt"
    					#print itt[1]
    					#print str[i]
    					#print i
    					return 0
    			for letter in ea:
    				if str[i]==letter:
    					#print "here"
    					return 0	
   	return 1
    
    
    
    def p_evidence():
    	p_e=0
    	for item in wordcount.items():
    		#print item[0]
    		#print "hi"
    		#if item[0] == "THREE":
    		#	print "THREEeeeee" 
    		#	print item[0]
    		#pegw=p_evidence_given_word(item[0])
    		#if pegw==1:
    		#	print "hello" 
    		#pw=p_word(item[0])
    		#if pw >0:
    		#	print "hhhhhiiiiii"
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
    
    print "hix	"
    print p_l_given_evidence("E");
    #print p_l_in_word("THREE","J");
    #print p_word_given_evidence("THREE")
    #print p_evidence()	
    #print p_evidence_given_word("THREE")
    #print p_evidence_given_word("triab")
    #print p_evidence_given_word("trywb")
    #print p_evidence_given_word("tryme")
    #print p_evidence_given_word("ijkab")
    #print p_evidence_given_word("abtry")
    #print p_evidence_given_word("tayby")
    #print p_word(sorted_value[len(sorted_value)-1][0])
    #print p_word(sorted_value[0][0])

    
    
    
    
        
    
    
    
    
    
    
    

