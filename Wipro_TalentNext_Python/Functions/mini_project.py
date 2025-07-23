
# Functions/Modules/Packages

'''Project: 1
Write a Python function that accepts a hyphen-separated sequence of colors
as input and returns the colors in a hyphen-separated sequence after sorting
them alphabetically.

Constraint: All the colors will be completely in either lower case or upper case.
Sample input 1: green-red-yellow-black-white
Sample output 1: black-green-red-white-yellow

Sample input 2: PINK-BLUE-TAN-PURPLE
Sample output 2: BLUE-PINK-PURPLE-TAN
'''

def ascend_words(str):
    split = str.split("-")
    print(split)
    split.sort()
    print(split)
    str2 = "-".join(split)
    return str2
    pass

str = input("Enter list of anything seperated by (-) : ")

print(ascend_words(str))
# ******************************************************************************************************

'''Project: 2
Create a Python module with the following functions:

Function Name

Task

ispalindrome(name):
Given the user name as input, this function should
tell us whether the name is a palindrome or not.


count_the_vowels(name) : 
Given the user name as input, this function should
tell us how many vowels are present in it.


frequency_of_letters(name):
Given the user name as input, this function should
tell us how many times each letter appears in the
name.

Note: name will be completely in either lower case or upper case.
Import the module in another python script and test the functions by passing
appropriate inputs.
Sample input 1: bob
Sample output 1:
Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1

'''

def ispalindrome(name):
    rname = ""
    for i in range(len(name)) :
        rname += name[i][::-1]
    if name == rname:
        print("Yes,Its a palindrome!")
    else : 
        print("No,Its not a palindrome!")    
    pass
name = "naman"
def num_vowel(name):
    count = 0
    vowel ="AEIOUaeiou"
    for i in range(len(name)):     
        if name[i] in vowel :
            count +=1           
    print (count)
    pass

def freq(name):
    count = {}
    name = name.lower()
    for i in name:
        if 'a' <= i <= 'z':
            count[i] = count.get(i,0)+1
    return count    
    pass
ispalindrome(name)
num_vowel(name)
print(freq(name))

