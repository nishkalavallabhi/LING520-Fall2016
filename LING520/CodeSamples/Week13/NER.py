import nltk
from nltk import word_tokenize

#sent = nltk.corpus.treebank.tagged_sents()[22]
#print(sent)
#print(nltk.ne_chunk(sent, binary=True))

test_sen = "Touré was born in 1939 in the village of Kanau, on the " \
        "banks of the Niger River in Gourma-Rharous Cercle in the " \
        "northwestern Malian region of Tombouctou. "
tagged_test_sen = nltk.pos_tag(word_tokenize(test_sen))
print(tagged_test_sen)
print(nltk.ne_chunk(tagged_test_sen, binary=True)) #To get NE or not NE
print(nltk.ne_chunk(tagged_test_sen)) #To get exact NE types. GPE - geo political entity.
