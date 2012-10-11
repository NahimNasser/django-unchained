from nltk.corpus import stopwords

lstopwords = stopwords.words(fileids='english')
SDICT = set()
for word in lstopwords: set.add(word.lower())