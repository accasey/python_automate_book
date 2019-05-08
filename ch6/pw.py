#! python3
# pw.py - an insecure password locker program 
import sys
import pyperclip

PASSWORDS = {'email': 'kjdbfskdjbskjdfbskdbf',
             'blog': 'ljdfsljdnsljdfnsldjnf',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# first command line arg is the account name
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for', account, 'copied to the clipboard')
else:
    print('There is no account named', account)