"""
This program uses the dictionary created in dictionary creation python file.
"""

def read_trigram_dict():
    trigram_counts = {}
    fh = open("ibsen-trigrams-dict.txt")
    for line in fh:
        key,value = line.split("\t")
        trigram_counts[key] = value
    fh.close()
    return trigram_counts

trigram_dict = read_trigram_dict()

user_input = input("Enter a trigram: ")
if user_input in trigram_dict.keys():
    print("This is a Ibsen trigram. It occurred", trigram_dict[user_input], " times in the corpus")
else:
    print("This is not a Ibsen trigram")
