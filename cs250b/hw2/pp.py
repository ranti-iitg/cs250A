from sklearn.datasets import fetch_20newsgroups                                       
categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']     
twenty_train = fetch_20newsgroups(subset='train',categories=categories, shuffle=True, 
random_state=42)                                                                      
                                                                                      
                                                                                      
from sklearn.feature_extraction.text import CountVectorizer                           
count_vect = CountVectorizer(stop_words='english')                                    
X_train_counts = count_vect.fit_transform(twenty_train.data)                          
                                                                                      
from sklearn.feature_extraction.text import TfidfTransformer                          
tfidf_transformer = TfidfTransformer()                                                
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)                       
                                                                                      
tfidf=X_train_tfidf.sum(axis=0)                                                       
list1=tfidf.tolist()                                                                  
list2=list1[0]                                                                        
list3=sorted(range(len(list2)), key=lambda i: list2[i])[-100:]                        
list4=[]                                                                              
for ll in list3:                                                                      
        for key in count_vect.vocabulary_:                                            
                if count_vect.vocabulary_.get(key)==ll:                               
                        list4.append(key)                                             
                                                                                      
mystop=[]                                                                             
for key in count_vect.vocabulary_:                                                    
        if key in list4:                                                              
             i=0                                                                         
        else:                                                                         
                mystop.append(key)                                                    
                                                                                      
                                                                                      
                                                                                      
from sklearn.feature_extraction import text                                           
                                                                                      
stop_words = text.ENGLISH_STOP_WORDS.union(mystop)       
