import datetime

# 1) Write me Python code that generates all prime numbers between 0 and 100
for num in range(1,101):
    count = 0
    for i in range (2, num//2+1):
        if num % i == 0:
            count=+1
            break
    if count == 0 and num != 1:
        print('%d' %num, end = ' ',)
# 2) take a list of strings [‘banana’ , ‘apple’ , ‘zebra’, ‘raspberry’] and order it in alphabetical order

words = ['banana', 'apple', 'zebra', 'raspberry']
print(sorted(words))

# 3) generate (you will need to look up how to generate) two sets of numbers - A and B.
# Then determine which numbers are common to both sets.
list_A = [1,3,24,5,6,32,1,2,3,45]
list_B = [2,3,4,5,21,54,65,2,4,5]
set_A = set(list_A)
set_B = set(list_B)
print(set_A.intersection(set_B))

# 4) make a dictionary of people you know: record their names and birthdays.
# Then write a function which takes as input the names of any two people in your
# dictionary and tells me the difference in minutes between their birthdays.
# You MUST define a function to do this.

people = {'Joe': '1988/1/1', 'Tom':'1987/1/1'}

def difference_in_birthdays(name_one, name_two):
    date_one = people[name_one]
    date_two = people[name_two]
    format_date = '%Y/%m/%d'
    datetime_obj_one = datetime.datetime.strptime(date_one, format_date)
    datetime_obj_two = datetime.datetime.strptime(date_two, format_date)
    difference = datetime_obj_one - datetime_obj_two
    difference_min = difference.total_seconds()/60
    return difference_min
print(difference_in_birthdays('Joe','Tom'))



# 5) make a .txt file in your computer, this file should have at least a paragraph of text, import that into Python,
# make every odd numbered sentence in uppercase and every even sentence lowercase. Save this via Python as a new text file
# in the same directory as the old file. DO NOT overwrite the old file (hint: check out the nltk library)

# import nltk.data
# import nltk.tokenize
# nltk.download('punkt')
# # f = open('text_file.txt', 'x') #creates the file
# text_file = open('text_file.txt', 'r')
# # print(text_file.read())
# sentence_count = nltk.sent_tokenize(text_file)
# print(sentence_count)


# 6) Look at the numpy library, import this into your Python session and
# construct 2 numpy arrays, multiple then together, what happened?
import numpy as np
# when arrays are same shapes
arr_one = np.array([1, 2, 3, 4, 5])
arr_two = np.array([6,7,8,9,10])
print(np.multiply(arr_one, arr_two))

#when arrays are in diff shapes and need to be resized
#arange() is a function to specify the range and index starts with zero and doesnt include the last number
x2 = np.arange(9).reshape((3,3))
print(x2)
x3 = np.arange(3)
print(x3)
print(np.multiply(x2, x3))

# 7) given a list of numbers [38, 42, 53, 94, 1, 3, 4, 79]
# return me a list of ones and zeroes where a 1 signifies
# If the number in the element is divisible by 2 with no remainder.
# So your answer should be [1, 1, 0, 1, 0, 0, 1, 0]
list_of_numbers = [38, 42, 53, 94, 1, 3, 4, 79]
new_list = []
for i in list_of_numbers:
    if i % 2 == 0:
        new_list.append(1)
    else:
        new_list.append(0)
print(new_list)

# 8) Count words in a string.
# E.g. “This is a string and you must count words in this”

# 9) count how many times each value is in a list
# (use base Python for this, don’t import Counter)
# 10) given a list,
# return a deduped list while maintaining its order
