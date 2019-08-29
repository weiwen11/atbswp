# \d digit, \d{3}, (ha){3}
# ? 0 or 1, * 0 or more, + 1 or more
import re


def isPhoneNumber(num):
    phoneRegex = re.compile(r'(\(\d{3}\)-)?(\d{3}-\d{4})')
    mo = phoneRegex.search(num)  # return MatchObject, match anywhere
    # mo = phoneRegex.match(num)  # match from beginning
    print(mo.group(1))
    print(mo.group(2))
    # a, b = mo.groups()  # groups return as tuple
    # mo2 = re.match(r'(.*)or(.*)', num)  # any before or, any after or
    # print(mo2.group(1))
    # print(mo2.group(2))


isPhoneNumber('abc 010-123-5533 or (010)-111-2222')
name = 'avdul'

# string format ways
print(f'{name} says hi')  # 3.6
print('%s says hi' % name)
print('{0} says hi'.format(name))

# default regex greedy (match longest string), use ? to mark nongreedy
nongreedy = re.compile(r'(ha){3,5}?')  # will match 3 ha

# regex.findall will return list of match / list of tuple groups
# character class: \d \w (a word, alnum, underscore) \s (space newline)
# custom char class: [0-9a-zA-Z] [wee] [^0-5] not 0-5
# ^ startswith endswith $
theWorldre = re.compile(r'^the.*world$')
print(theWorldre.search('the hello world'))

# . match any char except newline
nameRegex = re.compile(r'Name: (.*)')
print(nameRegex.search('Name: Alex').group(1))

# re.compile(r'.*', re.DOTALL | re.I | re.verbose)
# re.DOTALL will match newline
# re.I flag ignore case
# re.verbose add comments for multiline regex
re.compile(r'''
(\d{3})?  # test
(\s|-|\.)?
\d{3}
''', re.VERBOSE)

censorRegex = re.compile(r'Agent (\w)\w+', re.I)
print(censorRegex.sub(r'Agent \1*****', 'Agent Billy killed the man'))
