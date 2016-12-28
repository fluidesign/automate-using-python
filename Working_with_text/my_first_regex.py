# my first regex app
import re

oneDigitRegex = re.compile(r'\d') # we have to use raw due to escape chars such as \. so use r, "" or \\
getAllDigits = oneDigitRegex.findall('My number is 7 and 5')
print (getAllDigits)

oneDigitAndFollowingRegex = re.compile(r'\d(.*)')
getDigitAndTheRest = oneDigitAndFollowingRegex.search('Im 7 years old')
print(getDigitAndTheRest.group())