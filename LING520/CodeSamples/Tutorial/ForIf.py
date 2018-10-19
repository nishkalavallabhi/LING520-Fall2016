'''
Take a string as input from user, and print every 3rd character in the string, if it is not a "a"
Example: intelligentsia should print: t l e s
'''
def eg1():
    str = input("Enter a string that is more than 6 characters long: ")
    if len(str) <=6:
        print("Please read what I asked for. I am quitting!")
    else:
        count = 1
        for i in range(0, len(str)):
        #what I need here: I should print characters at indices 2,5,8,11,...
        # Not 0,3,6,9... I said: "Every third character".
            if count != 3:
                count = count +1
            else:
                if str[i] != 'a':
                    print(str[i])
                    count = 1
#I am not adding detailed comments. It is your job to figure out what these lines are doing!

'''
Implement a Caesar cipher encoder. Caesar cipher is a simple encryp-
tion technique named after Julius Caesar, who used it to communicate
with his team in cryptic messages. Usually, Ceasar cipher refers to any
encryption where each letter is replaced by another letter a fixed num-
ber of places down in the alphabet. For example, if the fixed number
is 3, A becomes D, B becomes E and so on. Now, your program should
implement a Ceasar cipher of the fixed size 4. Leave the punctuation
markers unchanged. Your input will be a normal English sentence,
and the output should be a Caesar cipher.
'''
#Implements a Caeser cipher for distance 2:
def eg2():
    str = input("Enter a string: ").lower()
    output = ""
    for char in str:
        if char == 'y':
                output = output + 'a'
        elif char == 'z':
                output = output + 'b'
        else:
            code = ord(char)
            output = output + chr(code+2)
    return output


#eg1()
print(eg2())

