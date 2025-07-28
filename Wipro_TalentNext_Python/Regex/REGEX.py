# Write a program to find check if a string has only octal digits. Given string [ '789', '123 ','004']

import re 
def is_octal (s) :
    return re.fullmatch(r'[0-7]+' , s.strip()) is not None 


string =  [ '789', '123 ','004']

for s in string : 
    if is_octal(s):
        print(f"{s} is an octal number ")
    else:
        print(f"{s} is not an octal number ")

#*************************************************************************************************************************************************
#  Extract the user id, domain name and suffix from the following email addresses.
'''
EMAILZ:
zuck@facebook.com
sunder33@googIe. com
jeff42@amazon.com
'''

import re
emails_ = '''
zuck@facebook.com
sunder33@googIe. com
jeff42@amazon.com
'''

email_pattern = r"(.*)@(.*)\.(.*)"
email_list = emails_.strip().split('\n')

for email in email_list : 
    cleaned_email = email.replace(' ', '').lower()

    match = re.search(email_pattern,cleaned_email)

    if match :

        userId , DomainName , suffix = match.groups()
        #   user_id, domain_name, suffix = match.groups()

        print(f'Original = {email} : ')
        print (f'USer id : {userId}')
        print (f'Domain name : {DomainName}')
        print (f'Suffix : {suffix}\n')

# **********************************************************************************************************************************************


# Split the following irregular sentence into proper words 
# sentence =  A, very   very; irregular__sentence"""
## expected outout : A very very irregular sentence

import re 

sentence = "  A, very   very; irregular__sentence"

words = re.split (r'[^a-zA-Z0-9]+' , sentence)

words = [word for word in words if word]

cleaned_sentence  = " ".join(words)

print (cleaned_sentence)

#****************************************************************************************************************************************************


# Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
# #tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today
# http://t.co/lbwej0px0d cc: @garybernhardt #rstats'''
# ##desired_output = 'Good advice What I would do differently if I was learning to code today'

import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

text = re.sub(r'http\S+', '', tweet)
print (text)#remove url from the tweet 
print("\n\n")

text = re.sub(r'[@#]\w+', '', text)
print (text)#remove @(@garybernhardt) and #(#rstats) from the tweet 
print("\n\n")

text = re.sub(r'\b(RT|cc)\b', '', text, flags=re.IGNORECASE)
print (text)#remove ct and RT from the tweet 
print("\n\n")

text = re.sub(r'[^\w\s]', '', text)
print (text)#remove all non alphanumeric character from the tweet 
print("\n\n")

cleaned_tweet = ' '.join(text.split())

print(cleaned_tweet)#final product

#****************************************************************************************************************************************************
# Extract all the text portions between the tags from the following HTML page:
# https://raw.githubusercontent.com/selva86/datasets/master/sample.html
# Code to retrieve the HTML page is given below:
# import requests
# r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
# r.text # html text is contained here

# desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph!', 
# 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']

import re 
import requests
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
r = requests.get(url)
html_c = r.text 

regex = r"<(?!\/)(?!!--)(.*?)>(.*?)<\/(.*?)>"

matches = re.findall(regex , html_c)

op = [match[1] for match in matches ]
print (op)


#********************************************************************************************************************************************
# Given below list of words, identify the words that begin and end with the same character.
# civic
# trust
# widows
# maximum
# museums
# aa
# as

import re

matching_word = []
words = ['civic','thrust', 'windows','maximum','museums','aa','as']

regex = r"^(.).*\1$|^.$"

for word in words :
     if re.match(regex,word):
        matching_word.append(word)

print(matching_word)     
#**************************************************************************************************************************************************
