import random


def nRandom(n):
    randList = []  # local scope
    for __ in range(n):  # __ throwaway var
        # print(random.randint(0, 1), end=' ')
        randList += [random.randint(0, 1)]  # list append
    print(randList)


def foo():
    global bar  # uses bar from global scope
    bar = 'hi'

def divide(n):
    try:
        return 5 / n
    except ZeroDivisionError:
        return 'Invalid argument.'


nRandom(3)
print(nRandom(2) == None)
print('a', 'b', 'c', sep=',')
bar = 'bye'
foo()
print(bar)
print(divide(5))
print(divide(0))
print()

# number guessing game
low = 0
high = 100
ans = random.randint(low + 1, high)
n = 0
print('Guess a number between ' + str(low) + ' and ' + str(high))
while True:
    print('Take a guess: ' , end='')
    try:
        guess = int(input())
    except ValueError:
        print('Invalid number')
        continue
    n += 1
    if guess == ans:
        print('Correct in ' + str(n) + ' tries.')
        break
    if guess < ans:
        print('Your guess is too low')
    elif guess > ans:
        print('Your guess is too high')

