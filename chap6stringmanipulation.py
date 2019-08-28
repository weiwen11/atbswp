import pyperclip
print('Hello\'s hi \nhi')
print(r'Hello\'s hi \nhi')  # raw string
print()
# tripple quote multiline string
print('''Dear Bobby,

\tI miss Bob's cat. # asdf

Sincerely,
Bob''')
print()

"""
This is a
multiline
comment
"""

# string slice same as list slice
foo = 'The world'
print(foo[::-1])
print(foo[4:])

# in / not in
print('The' in foo)
print('' in foo)
print(' world' in foo)
print('THE' not in foo)

# upper lower isupper islower and etc
print(foo.upper())
print(foo.lower())
print(foo.upper().isupper())
print(foo.islower())

# startswith endswith
print(foo.startswith('The'))
print(foo.endswith('ld'))

# join split
print(foo.split('w'))
print(','.join(['cat', 'dog', 'mom']))

# rjust center ljust
print(foo.rjust(30, '['))
print(foo.center(20, '*'))
print('Nasi Lemak'.ljust(20, '.') + str(6.5).rjust(6))

# strip rstrip lstrip
print('   hi hi    '.strip())
print('---aa--'.lstrip('-'))

# pyperclip access system clipboard
# pyperclip.copy('The world')

# print(pyperclip.paste())

# table printer
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(aList):
    for i in range(len(aList[0])):
        for j in range(len(aList)):
            longest = len(max(aList[j], key=len))
            print(aList[j][i].rjust(longest+1), end='')
        print()


printTable(tableData)
