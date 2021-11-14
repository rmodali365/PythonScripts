import random
def reverseWord(word):
    reverseWord = ''
    for x in range(1,len(word)+1):
        reverseWord+=word[len(word)-x]

    print(reverseWord)


reverseWord('hello')


def reverseString(sentence):
    reverseString = ''
    stringList = sentence.rsplit(" ")
    print(stringList)
    for x in stringList:
        reverseString = x + ' '+ reverseString
    print(reverseString)


reverseString('Hello my name is Rushil')

x = random.randint(0,100)
print(x)

