# !python3

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code can be 3 digits or 3 digits within 
(\s|-|\.)? # separator 
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE) 
## groups -> 1:area. 2:seperator. 3: 3 digits. 4: seperator. 
## 5. last 4 digits 6. ext . 7 space. 8 ext number

emailRegex = re.compile(r'''(([^@])+(@[^@]+\.[^@]+))''')

if emailRegex.match('''dima.aronov@tufin.com'''):
    print("ok")

clipboardTest = str(pyperclip.paste())
# define group
matches = []

for match in phoneRegex.findall(clipboardTest):
    ## debug
    for i in range (len(match)):
        print(str(i) + ' ' + match[i],end='  ')
    phoneNum = '-'.join([match[1], match[3], match[5]])
    print(phoneNum)
    if match[8] != '':
        phoneNum += ' x' + match[8]
    matches.append(phoneNum)
for match in emailRegex.findall(clipboardTest):
    for i in range (len(match)):
        print(str(i) + ' ' + match[i],end='  ')    
    matches.append(match[0])
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Output: ')
    print('\n'.join(matches))
else:
    print('No phone number or email were identified in the clipboard')