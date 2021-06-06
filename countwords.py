word = input("enter word")
wordCount = 1
characterCount = 0

for i in word:
    characterCount = characterCount+1
    if(i==' '):
        wordCount = wordCount+1
print("number of characters:")
print(characterCount)
print("number of words:")
print(wordCount)