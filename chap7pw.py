# password validator
import re
strength1 = re.compile(r'([a-z])')
strength2 = re.compile(r'([A-Z])')
strength3 = re.compile(r'([0-9])')
strength4 = re.compile(r'([!-/:-@[-`{-~])')
strength5 = re.compile(r'.{8,}')

pw = input('Password: ')
strength = 0
if strength1.search(pw):
    strength += 1
if strength2.search(pw):
    strength += 1
if strength3.search(pw):
    strength += 1
if strength4.search(pw):
    strength += 1
if strength5.search(pw):
    strength += 1

if strength == 0:
    print('Invalid password')
elif strength in [1, 2]:
    print('Weak password')
elif strength in [3, 4]:
    print('Normal password')
elif strength == 5:
    print('Strong password')
