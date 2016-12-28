#! python3
# Adding char to a beggining of each line pasted from the clipboard
#import section
import pyperclip
#
text = pyperclip.paste()

lines = text.split('\n') # split the text to lines 
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)