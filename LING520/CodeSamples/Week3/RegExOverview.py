#mbox-short.txt source: http://www.py4inf.com/code/mbox-short.txt

'''
Purpose:
a) Illustrate the use of search, match, findall, sub, subn functions.
b) Illustrate the use of flags: MULTILINE and DOTALL
c) Illustrate the use of ? operator
'''

import re


#print(re.match("a","baba")) #Returns none
#print(re.search("a","baba")) #Returns a match object
#print(re.fullmatch("a","baba")) #returns none

fh = open("example.txt")

#Prints lines having "th" after a space
for line in fh:
    if re.search(" th",line):
        #print(line)
        print()

#Prints a list of matches for re.*RegEx, spanning two lines.
content = open("example.txt").read()
temp = re.findall("sometimes.*difficult",content,re.DOTALL) #remove re.DOTALL and try.
#print(temp)

#re.MULTILINE overview.
temp2 = re.findall("^This",content,re.MULTILINE) #Remove re.MULTILINE or replace with re.DOTALL and try.
#print(temp2)

#re.sub() overview
temp3 = re.sub("Th", "HA", content) #replace sub with subn and try
#print(temp3)

#For more details on other re functions, visit: https://docs.python.org/3/library/re.html
