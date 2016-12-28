## char counter
import pprint

count = {}
message = "Hello, lets count the number of chars in the string"
print ('Let me count for you the number of appearances of each letter in the message')

for secretChar in message:
    count.setdefault(secretChar,0)
    count[secretChar] = count[secretChar] +1

print(count)
pprint.pprint(count)