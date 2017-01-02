# !python3
# Strong password protection
import re

strongPasswordRegex = re.compile(r"((?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*))")

print ('####### Strong password protection#######')
print ('Testing:\n8 chars long\nboth upper and lower\natleast one digit')
while True:
    print('Type a password you wish to test or blank to exit:')
    password = str(input())
    if (len(password) != 0):
        if strongPasswordRegex.match(password):
            print('Password OK')
        else:
            print('Password NOK.')
    else:
        print('Thank you')
        break;