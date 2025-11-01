#Word Frequency Counter of each word

str=input("Enter your Sentence: ")

str=str.lower()

word=str.split()

for word in str.split():
    print(f"{word}",str.split().count(word))