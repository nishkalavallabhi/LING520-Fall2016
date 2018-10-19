#Source: http://www.katrinerk.com/courses/python-worksheets/language-models-in-python
#My edit: I am adding extra code towards the end to illustrate trigram models, and some extra comments here and there.
#Sowmya, 21st October 2016.

'''
What this does: Shows how to build a small bigram, and a trigram language model in NLTK. This example uses Brown corpus
which is available within NLTK. But you can use any corpus you want as long as you convert it to a list of tokens.
NLTK allows you to do that too, and if you remember, that was one of things you did in the class in Week 2 or 3.
'''

import nltk
from nltk.corpus import brown
#imports: Brown university corpus of present day American English.

'''
nltk.FreqDist() is a function that takes a list of word strings and returns a frequency distribution i.e., words and their counts in the list,
in the descending order of counts.
brown.words() is a function implemented for that Brown corpus, that returns the corpus as a list of word tokens.
'''
brown_unigrams = nltk.FreqDist(brown.words()) #Just unigram frequency distribution.
#brown_bigrams = nltk.bigrams(brown.words())
#brown_trigrams = nltk.trigrams(brown.words())

#Getting unigram probability for a given word.. let us say "my" again.
def unigram_prob(word):
    return brown_unigrams[word]/len(brown.words())
print("unigram prob. of my", unigram_prob('my'))

for unigram, count in brown_unigrams.items():
    print(unigram, count)

