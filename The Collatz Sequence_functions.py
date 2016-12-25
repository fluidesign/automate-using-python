## Collatz sequence

def collatz(num):
    ## if number even will divide by 2 and return
    ## if number odd will mult *3, add +1 and return
    if ((num % 2) == 0):
        return int(num / 2)
    else:
        return int((num * 3) + 1)
    
print('#####The collatz Sequence Start#####')
print('Please choose a number')

try:
    userNumber=int(input())
    print('You chose: ' + str(userNumber))
    outputNumber=userNumber
    while (outputNumber > 1):
        outputNumber = collatz(outputNumber)
        print('Number after collatz function: ' + str(outputNumber))
except ValueError:
    print('ValueError, you must write an integer')

print('#####The collatz Sequence End#####')
