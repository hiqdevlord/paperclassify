#encoding=utf-8
import nltk,re,pprint,jieba
import jieba.posseg as pseg
import codecs
import sys
from nltk.corpus import names
import random
global stop

#reload(sys)
#sys.setdefaultencoding( 'utf-8' )

#金标准 1.0
def type_features0(word):
    return {'first_two_letter':word[:2]}

#第一个名词 0.40925
def type_features1(word):
    f = open(word)
    sentence = f.read()
    wordlist = pseg.cut(sentence)
    for w in wordlist:
        if w.flag.startswith('n'):
            return {'firstn':w.word}

#所有的名词 0.89680
def type_features2(word):
    f = open(word)
    sentence = f.read()
    wordlist = pseg.cut(sentence)
    features = {}
    for w in wordlist:
        if w.flag.startswith('n'):
            features['contains(%s)' % w.word] = w.word
    return features
#第一个词 0.28114
def type_features3(word):
    f = open(word)
    sentence = f.read()
    wordlist = pseg.cut(sentence)
    for w in wordlist:
        return {'firstw':w.word}

#所有的词 0.73666
def type_features4(word):
    f = open(word)
    sentence = f.read()
    wordlist = pseg.cut(sentence)
    features = {}
    for w in wordlist:
        features['contains(%s)' % w.word] = w.word
    return features

#所有的非停止词 0.80071
def type_features5(word):
    f = open(word)
    sentence = f.read()
    wordlist = pseg.cut(sentence)
    features = {}
    for w in wordlist:
        if w.word not in stop:
            features['contains(%s)' % w.word] = w.word
    return features

#所有非停止词的名词 0.87189
def type_features6(word):
    f = open(word)
    sentence = f.read()
    wordlist = pseg.cut(sentence)
    features = {}
    for w in wordlist:
        if (w.word not in stop) and (w.flag.startswith('n')):
            features['contains(%s)' % w.word] = w.word
    return features

#所有停止词  
def type_features7(word):
    f = open(word)
    sentence = f.read()
    wordlist = pseg.cut(sentence)
    features = {}
    for w in wordlist:
        if w.word in stop:
            features['contains(%s)' % w.word] = w.word
    return features

def type_name(word):
    if word.startswith('5'):
        return 'ENV'
    if word.startswith('10'):
        return 'PHY'
    if word.startswith('4'):
        return 'TRA'
    if word.startswith('3'):
        return 'EDU'
    if word.startswith('6'):
        return 'ECO'
    if word.startswith('8'):
        return 'MIL'
    if word.startswith('1'):
        return 'COM'
    if word.startswith('7'):
        return 'MED'
    if word.startswith('2'):
        return 'ART'
    if word.startswith('9'):
        return 'POL'
flist = open("list.txt")
lista = flist.read().split('\n')
#print lista
bbs = ([(w,type_name(w)) for w in lista if w.endswith('txt') or w.endswith('TXT')])
#print bbs
fin = open("stop.txt")
s = jieba.cut(fin.read())
stop = [w for w in s]
random.shuffle(bbs)
featuresets = [(type_features2(n),g) for (n,g) in bbs]
size = int(len(featuresets)*0.1)
train_set = featuresets[size:]
test_set = featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier,test_set)
























