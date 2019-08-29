# extracts phone number and email with regex
import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # optional area code
    (-|\s|\.)?          # optional separator
    (\d{3})
    (-|\s|\.)
    (\d{4})
    \s*((ext|x|ext.)\s*(\d{2,5}))?  # optional extension
    )''', re.VERBOSE)

# print(phoneRegex.findall('808.123.1234 x 404'))
emailRegex = re.compile(r'''(
    ([a-zA-Z0-9._%+-]+)  # before @
    @
    ([a-zA-Z0-9.-]+)     # domain
    (\.[a-zA-Z]{2,4})    # dotcom
    )''', re.VERBOSE)
# print(emailRegex.findall('hihi coolkid42069@gmeil.kom'))
text = pyperclip.paste()

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

print('\n'.join(matches))
