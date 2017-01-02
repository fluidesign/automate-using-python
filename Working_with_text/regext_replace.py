# !python3
## regext replace - http://www.regexr.com/
import re

namesRegex = re.compile(r'Agent \w+')
output = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(output)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
output = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(output)

## writing a complex regex with a detailed programming style
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

output = phoneRegex.search('555-345-6543')
print(output.group())