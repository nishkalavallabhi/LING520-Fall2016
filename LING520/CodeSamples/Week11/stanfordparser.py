from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
import pprint

#Folder on your desktop which you unzipped after downloading Stanford parser.
parser_folder = "/home/bangaru/Downloads/stanford-parser/"

'''To use Stanford parser in NLTK, you need two file paths: path to a .jar file called stanford-parser which has all the
parser code written in Java, and another file which ends in -models.jar (exact name may look different depending on
when you downloaded. This file has all the trained PCFG parser models. We can use any model to get the parse tree.
'''
parser_jar = parser_folder + 'stanford-parser.jar'
models_jar = parser_folder + 'stanford-parser-3.6.0-models.jar'

#This is how the StanfordParser object is initiated.
#There is an optional third parameter you can give here, which is model_path.
#Use that if you do not want the default constituency parser and want to try others.
const_parser = StanfordParser(parser_jar, models_jar) #model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
#Model path is relative to your models_jar path. So, you don't have to start from /home/user whatever.
#In the above example, the only thing you change for model path will be: englishPCFG.ser.gz - instead of that, there may be other models.

#This is how we call a dependency parser object. again, you can optionally specify a model_path variable.
dep_parser = StanfordDependencyParser(parser_jar, models_jar)

#Learnt the usage from commented lines in NLTK documentation for stanford parser
#http://www.nltk.org/_modules/nltk/parse/stanford.html

#Example constituent parse
const_output = const_parser.raw_parse("This is a sentence.")
print("Printing an example constituent structure output")
for item in const_output:
    print(item)

#Example Dependency parse
print() #Prints emptyline
print()
print()

[parse.tree() for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")]

print("Printing an example dependency structure output")
dep_output = dep_parser.raw_parse("The nice boys in the nice house have a nice toy.")
#print(type(dep_output))

for item in dep_output:
    print(type(item))
    print(item.to_conll(4))
    print(item.left_children(8))
    #pprint.pprint(list(item.triples()))

#Note to all: I tried all sorts of things before reaching here and it took a lot of time.
# Don't imagine I magically figured this out.
#When you should work with a new code, you will experience this process again and again
# even if you do code for a living for 50 years.

#What you can do:
#1. Explore what possible outputs can we print apart from syntactic parses (parses with likelihoods, for example)
#2. Explore different parser models: go through the README, extract the models.jar file to see options etc.
