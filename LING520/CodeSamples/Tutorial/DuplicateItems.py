#Purpose: Identify duplicate items in a list.

"""
This program will take a list as input and print out a sub-list, which has only those elements that repeat in the list.
So, if [2,3,4,2,1,121,3] is given as input, [2,3] is given as output.
Note: There are multiple ways of doing this. I am just showing one of them.
"""

'''
This small function takes a list as input and returns a subset of this list containing duplicate items as output.
'''
def duplicates(some_list):
    result_list = []
    seen_items = []
    for item in some_list:
        if item not in seen_items:
           seen_items.append(item)
        else:
           result_list.append(item)
    return result_list

'''
Alternative way of doing the same thing above, which preserves the order of appearance of items.
'''
def duplicates2(some_list):
    result_list = []
    for item in some_list:
        if some_list.count(item) > 1 and (item not in result_list):
            result_list.append(item)
    return result_list

#This line below takes a comma separated number string from user, and converts it to a list object
input_list = [int(x) for x in input("Enter a bunch of numbers, separated by comma: ").split(",")]

'''
Longer version of the above code. The above line is called 'List comprehension' in Python.
input_list = []
user_input = input("Enter a bunch of numbers, separated by comma: ").split(",")
for x in user_input:
    input_list.append(int(x))
'''

#Bunch of print statements to show output.
print("Your input: ", input_list)
print("Duplicate items in list are: ", duplicates(input_list))
print("Duplicate items in list using another method are: ", duplicates2(input_list))

