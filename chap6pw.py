#! python3
import sys
import pyperclip

PASSWORDS = {'email': 'abcd1234',
             'game': '1234abcd'}

if len(sys.argv) < 2:
    print('Usage: python chap6pw.py [account] - copy account password')
    sys.exit()

pyperclip.copy(PASSWORDS.get(sys.argv[1], 0))
if sys.argv[1] not in PASSWORDS:
    print('There is no account named ' + sys.argv[1])
