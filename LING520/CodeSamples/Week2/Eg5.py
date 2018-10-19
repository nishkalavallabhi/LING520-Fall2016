content = open("sample.txt").read()
print(content)
added_text = "I am going to add this to the file now."
file = open("sample.txt", "a")
file.write(added_text)
#I am not closing the file handlers - you should!
