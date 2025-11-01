#Remove Puctuation from String.
#Write a Python program to  remove all punctuation characters from a string using string methods or the string Module.

import string

sentence=input("Input Your Sentence:")
Clean_sentence=sentence.translate(str.maketrans("","",string.punctuation))
print(Clean_sentence)