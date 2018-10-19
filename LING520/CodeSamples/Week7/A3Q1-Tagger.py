probs_list = []

#Reading in the file I created from Program 1.
#Why am I reading this as List? I did not figure out yet how to search optimally with substrings in a large dictionary.
def read_trained_probs():
    fh = open("A3Q1-Trained-2.txt")
    for line in fh:
        probs_list.append(line.replace("\t"," ")) #So that each item is of the form: TAG WORD COUNT or its TAG WORD TAG COUNT
    fh.close()
    return probs_list

#Takes a look at all possible ngrams (TAG1 WORD2 TAG2) sequences, and returns the one that has max count in data.
def return_max_count_tag(tag_options):
    max_count_index = 0
    max_count = 0
    for item in tag_options:
        if len(item.strip().split(" ")) > 3:
            temp_count = int(item.strip().split(" ")[-1])
            if temp_count > max_count:
                max_count = temp_count
                max_count_index = tag_options.index(item)
    return tag_options[max_count_index]

def do_tagging(input_sen):
    words = input_sen.split(" ") #For demo, I am assuming plain white space stripping will work.
    print(words)
    tags = []
    #We want: S_BEGIN, WORD1 - to get Tag 1; Tag 1, Word 2 to get Tag 2; Tag2, Word 3 to get Tag 3 etc.
    for i in range(0,len(words)):
        if i == 0:
            #We need: Tag 1 possibilities
            searching_prob = "S_BEGIN " + words[0] + " "
        else:
            searching_prob = tags[i-1] + " " + words[i] + " "
        tag_possib = [ngram for ngram in probs_list if ngram.startswith(searching_prob)]
        print(words[i])
        print(tag_possib)
        if len(tag_possib) > 0:
            tag = return_max_count_tag(tag_possib).strip().split(" ")[-2]
            tags.append(tag)
            print(tag)
        else:
                tags.append("NNP")
    return tags

def main():
        probs_list = read_trained_probs()
        while True:
            input_sen = input("Enter a new sentence: ")
            if input_sen == "stop":
                print("Thanks for using this. Stopping the program now")
                exit()
            tags = do_tagging(input_sen)
            print(tags)

if __name__ == '__main__':
    main()



