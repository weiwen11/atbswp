import pyperclip

lines = pyperclip.paste().split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

pyperclip.copy('\n'.join(lines))
print(pyperclip.paste())
