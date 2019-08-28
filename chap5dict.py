import pprint
import random
# dictionary key value pair
myDict = {'key': 5, 'size': 'big', 'hot': True,
          'point': {'x': 5.5, 'y': 10.3}}
print(myDict['key'])
print(myDict['point']['x'])

myStr = ''
for i in range(260):
    rand = random.randint(65, 90)
    myStr += chr(rand)

wordCount = {}
for c in myStr:
    wordCount.setdefault(c, 0)
    wordCount[c] += 1

pprint.pprint(wordCount)
# for i in range(100):
#     print(str(i) + ':' + chr(i), end=' ')

print([1, 2, 3] == [3, 2, 1])  # list order matter
print({'1': 1, '2': 2, '3': 3} == {'3': 3, '1': 1, '2': 2})  # dict any order

cost = {'iphone': 3000, 'samsung': 2000}

while False:  # off
    print('Enter a product: ', end='')
    name = input()

    if name == '':
        break

    if name in cost:
        print('Cost of ' + name + ' is ' + str(cost[name]))
    else:
        print('New product. Enter cost: ', end='')
        price = float(input())
        cost[name] = price
        print('Database updated')
        print()

print(cost)
for v in cost.values():
    print(v)

for k in cost.keys():
    print(k)

for k, v in cost.items():
    print(k, v)

print('iphone' in cost)
print(3000 in cost.values())

# use get to have default value if key not exist
print(cost.get('samsung', 0))
print(cost.get('nokia', 0))

# tic tac toe
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(b):
    print(b['top-L'] + '|' + b['top-M'] + '|' + b['top-R'])
    print('-+-+-')
    print(b['mid-L'] + '|' + b['mid-M'] + '|' + b['mid-R'])
    print('-+-+-')
    print(b['low-L'] + '|' + b['low-M'] + '|' + b['low-R'])


def checkWinner(b):
    if b['top-L'] != ' ' and b['top-L'] == b['top-M'] == b['top-R']:
        return True
    if b['mid-L'] != ' ' and b['mid-L'] == b['mid-M'] == b['mid-R']:
        return True
    if b['low-L'] != ' ' and b['low-L'] == b['low-M'] == b['low-R']:
        return True
    if b['top-L'] != ' ' and b['top-L'] == b['mid-L'] == b['low-L']:
        return True
    if b['top-M'] != ' ' and b['top-M'] == b['mid-M'] == b['low-M']:
        return True
    if b['top-R'] != ' ' and b['top-R'] == b['mid-R'] == b['low-R']:
        return True
    if b['top-L'] != ' ' and b['top-L'] == b['mid-M'] == b['low-R']:
        return True
    if b['top-R'] != ' ' and b['top-R'] == b['mid-M'] == b['low-L']:
        return True


turn = 1
while False:  # off game
    printBoard(theBoard)
    print('Turn ' + str(turn) + ' move: ', end='')

    move = input()
    if move not in theBoard or theBoard[move] != ' ':
        print('Invalid move')
        continue

    if turn % 2 != 0:
        theBoard[move] = 'X'
    else:
        theBoard[move] = 'O'
    turn += 1
    if checkWinner(theBoard):
        printBoard(theBoard)
        print('Win')
        break

# nested dict traversal
guests = {'Alice': {'Apple': 3},
          'Brax': {'Apple': 4, 'Orange': 2},
          'Cony': {'Orange': 2}}

numApple = 0
numOrange = 0
for k, v in guests.items():
    numApple += v.get('Apple', 0)
    numOrange += v.get('Orange', 0)

print(str(numApple))
print(str(numOrange))

# game inventory
inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1}
goblinLoot = ['arrow', 'arrow', 'gold coin',
              'wooden club', 'arrow', 'gold coin']


def displayInventory(i):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(v, k)
        total += v
    print('Total number of items:', total)


def addToInventory(i, loot):
    for k in loot:
        i.setdefault(k, 0)
        i[k] += 1


displayInventory(inventory)
addToInventory(inventory, goblinLoot)
displayInventory(inventory)
