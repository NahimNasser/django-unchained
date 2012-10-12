from nltk.corpus import stopwords

lstopwords = stopwords.words(fileids='english')
SDICT = set()
for word in lstopwords: SDICT.add(word.lower())

def remove_all_stop_words(wlist):
    new_list = wlist[:]
    for word in wlist:
        if (word in SDICT):
            new_list.remove(word)
    return new_list
    
def feature_extractor(obj):
    """
    Extract features from the object.
    """
    obj = obj.lower()
    
    pun_str = '!.|#{}[]<>"%*^-~/\\;:'
    for punc in pun_str:
        obj = obj.replace(punc,"")
    
    words = obj.split(' ')
    for word in words:
        if(word[:4]=='http'):
            obj = obj.replace(word,"")
    
    words = obj.split(" ")
    words = remove_all_stop_words(words)
    
    dic = {}
    for word in words: dic[word] = True
    
    return dic
    
import pickle
samples = pickle.load(open("pickle.txt"))
    
sgood = [(feature_extractor(sample),'good') for sample in samples['good']]
sbad = [(feature_extractor(sample),'bad') for sample in samples['bad']]

good_cutoff = 300
bad_cutoff = 300

train = sgood[:good_cutoff] + sbad[:bad_cutoff]
test = sgood[good_cutoff:] + sbad[bad_cutoff:]

import nltk
classifier = nltk.classify.NaiveBayesClassifier.train(train)
print nltk.classify.accuracy(classifier,test)


