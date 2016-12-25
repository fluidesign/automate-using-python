# comma code
# Write a function that takes a list value as an argument and returns a string with all the
# items separated by a comma and a space, with and inserted before the last item. For
# example, passing the previous spam list to the function would return 'apples, bananas,
# tofu, and cats'. But your function should be able to work with any list value passed to
# it.

specialIndex=-1
speicalWord='and '

def listToString(ourList):
    outputString=''
    ourList.insert(specialIndex, speicalWord)
    for i in range (len(ourList)):
        outputString += str(ourList[i])
        if (i < len(ourList)-2):
            outputString += str(', ')
    print(outputString)

spam = ['apples', 'bananas', 'tofu', 'cats']
listToString(spam)
spam2 = [1, 2, 3, 4]
listToString(spam2)
spam3 = [[spam], [spam2]]
listToString(spam3)
