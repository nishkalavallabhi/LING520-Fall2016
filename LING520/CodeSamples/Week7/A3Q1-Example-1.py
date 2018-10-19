import re

training_file_path = "/home/bangaru/Desktop/Teaching@ISU/FALL16/LING520/Assignments/Assignments/trainingdata-POSTagger.txt"
output_probs_storage = "A3Q1-Trained-2.txt"
dict_counts = {}

#word_tag_list is a list which has words of a sentence in this sequence: S_BEGIN, Word1, Tag1, Word2, Tag2 ... S_END
#We should have: Tri gram estimates for this input.
#This function extracts word-tag-word and tag-word-tag trigram combinations.
def add_counts(word_tag_list):
    for i in range(0, len(word_tag_list)-1):
        #bi_gram_temp = " ".join(word_tag_list[i:i+2])
        #dict_counts[bi_gram_temp] = dict_counts.get(bi_gram_temp,0) +1
        if i != len(word_tag_list)-2:
             tri_gram_temp = " ".join(word_tag_list[i:i+3])
             print(tri_gram_temp)
             dict_counts[tri_gram_temp] = dict_counts.get(tri_gram_temp,0) +1

def read_data():
    #Note: End of a sentence in this training file is indicated by a blank line.
    fh = open(training_file_path)
    sen_tags = []
    sen_tags.append("S_BEGIN")
    for line in fh:
        if line.strip() == "": #This indicates end of sentence
            sen_tags.append("S_END")
            add_counts(sen_tags)
            #print(sen_tags) #To see what the sentence sequence looks like.
            sen_tags = []
            sen_tags.append("S_BEGIN")
        else:
            sen_tags.extend(re.sub("\t|\s+"," ", line.strip()).split(" "))
    fh.close()

#Storing the trigrams dictionary into a file on my hard-disk.
def write_output():
    fwrite = open(output_probs_storage,"w")
    for key,value in dict_counts.items():
        fwrite.write(key+"\t"+ str(value))
        fwrite.write("\n")#You can store sorted file if you want.
    fwrite.close()

def main():
    read_data()
    write_output()

if __name__ == '__main__':
    main()

