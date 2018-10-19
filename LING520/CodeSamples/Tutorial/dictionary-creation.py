'''
This program takes a file ibsen.txt as input and outputs a file called ibsen-trigrams-dict.txt, which stores
the counts of trigrams in ibsen.txt
'''

import re
import string

training_file_path = "ibsen.txt"
output_dict_storage = "ibsen-trigrams-dict.txt"

output_dict = {} #Empty dictionary that will be used to store trigram counts.

fh1 = open(training_file_path)

for line in fh1:
    #What is this complicated line below doing??
    words_in_this_line = re.sub('['+string.punctuation+']', '', line.lower().strip()).split(" ")
    for i in range(0,len(words_in_this_line)-2):
        trigram = words_in_this_line[i] + " " + words_in_this_line[i+1] + " " +words_in_this_line[i+2]
        output_dict[trigram] = output_dict.get(trigram,0) +1
fh1.close()

print("Number of entries in trigram dict now is:" ,len(output_dict))

#Now below, I am storing the trigram dictionary I just created in to a text file in the same directory.
fh2 = open(output_dict_storage,"w")
for key,value in output_dict.items():
    fh2.write(key+"\t"+str(value))
    fh2.write("\n")
fh2.close()

