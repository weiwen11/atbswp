import random  # from random import *
import sys
# sys.exit()
isCold = False
isWarm = False

print(5 == '5')
print(True and False)
print(True or False)
print(not False)

if isCold:
    print('cold')
elif isWarm:
    print('warm')
else:
    print('hot')

n = 0
while n < 5:
    print(n)
    n = n + 1

# 0, 0.0, '' is False

# for i in range(3):  # 0 1 2
# for i in range(0, 10, 2):  # 0 - 8
for i in range(10, 0, -2):  # 10 - 2
    print(i)

total = 0
for num in range(101):
    total += num
print(total)

for i in range(5):
    print(random.randint(0, 1))

print(round(2.675, 2))
print(abs(-5))
