#! python3
# A program demonstrating how password manager working
# import section
import sys, pyperclip
#
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

if (len(sys.argv) < 2):
    print('Usage: py password_manager.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' was copied to the clipboard')
else:
    print("We could'nt find any password for " + account)

