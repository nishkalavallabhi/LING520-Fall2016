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
brown_bigrams = nltk.bigrams(brown.words())
brown_trigrams = nltk.trigrams(brown.words())

#Getting unigram probability for a given word.. let us say "my" again.
def unigram_prob(word):
    return brown_unigrams[word]/len(brown.words())
print("unigram prob. of my", unigram_prob('my'))

'''
nltk.ConditionalFreqDist() is a function that counts frequencies of pairs instead of single words as done in FreqDist()
When given a list of bigrams, it maps each first word of a bigram to a FreqDist over the second words of the bigram.
'''
cfreq_brown_2gram = nltk.ConditionalFreqDist(brown_bigrams)

#print(cfreq_brown_2gram.conditions())
#this above line will print all the starting words in a bigram in the corpus. .conditions() for this ConditionalFreqDist
#is like .keys() in a dictionary.

#This below print statement will print you all bigrams with my as the starting word.
#print(cfreq_brown_2gram["my"].keys())

#This below print statement will print you 5 most frequent bigrams that start with my
print("five most freq. words after my: ", cfreq_brown_2gram["my"].most_common(5))

#In NLTK, once you have such bigram frequency counts, you can get conditional probabilities like this.
cprob_brown_2gram = nltk.ConditionalProbDist(cfreq_brown_2gram, nltk.MLEProbDist)

#print("Probability of seeing 'my own': ", cprob_brown_2gram["my"].prob("own")) #This prints you the bigram probability: P(own|my)
#print("Probability of seeing 'my brother': ", cprob_brown_2gram["my"].prob("brother"))

#cprob_brown_2gram - is the bigram language model we have. We can use this to calculate the probability of a sentence.
#P(what do you do) = P(what) * P(do|what) * P(you|do) * P(do | you)
sentence = "what do you do"
prob_sentence = unigram_prob("what") * cprob_brown_2gram["what"].prob("do") * cprob_brown_2gram["do"].prob("you") * cprob_brown_2gram["you"].prob("do")
#print("Probability of a sentence 'what do you do'", prob_sentence) #will print: some very small number. approx 1.5*10^-9

#Now, how do we do this exact same thing, with trigrams instead?
'''
When adapting ConditionalFreqDist to trigrams, you need to tweek your trigram structure a little bit,
to make it look like two parts. ('my' 'name' 'is') should look like: (('my' 'name'), 'is')
'''
brown_trigram_condition_pairs = (((w0, w1), w2) for w0, w1, w2 in brown_trigrams)
print(brown_trigram_condition_pairs)
SystemExit
cfreq_brown_3gram = nltk.ConditionalFreqDist(brown_trigram_condition_pairs)
cprob_brown_3gram = nltk.ConditionalProbDist(cfreq_brown_3gram, nltk.MLEProbDist)

print("five most freq. words after 'my own': ", cfreq_brown_3gram[('my','own')].most_common(5))
print("Probability of seeing 'my own judgement': ", cprob_brown_3gram[('my', 'own')].prob("judgement"))
print("Probability of seeing 'my own house': ", cprob_brown_3gram[('my', 'own')].prob("house"))

prob_sentence_trigram = unigram_prob("what") * cprob_brown_2gram["what"].prob("do") * cprob_brown_3gram[('what','do')].prob("you") \
                        * cprob_brown_3gram[('do','you')].prob("do")
print("Probability of a sentence 'what do you do' according to trigram model", prob_sentence_trigram)
#print(freq_brown)
#print(freq_brown.most_common(20))

'''
#TODO: automate the prob_sentence_trigram line to work on any sentence from the user, and without showing a zero prob anytime.
#That is your job!

Logic:
1) tokenize the sentence into a list of words. You can remove punctuation if you don't want them.
2) task is to look through the list of words, and calculate prob_sentence and prob_sentence_trigram in the above code.
3) how? : you should start with a for loop, where each iteration considers the previous two words and the current word.
4) how 2: each time you finish one iteration of the loop, you should multiply your result to existing result (probability)
'''
