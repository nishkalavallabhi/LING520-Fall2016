import nltk

grammar3 = nltk.data.load('file:pcfg2.cfg', 'pcfg')
parser1 = nltk.ViterbiParser(grammar3)

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']

for tree in parser1.parse(sent):
  print(tree)


