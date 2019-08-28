import copy
print(bool([]))  # empty list false
print(bool(()))  # empty tuple false

#           0      1      2      3       4
#          -5     -4     -3     -2      -1
myList = ['Jon', 'Joe', 'Ken', 'Taki', 'Sam']
print(myList[::-1])  # list reversal
print(myList[-1:-6:-1])  # another list reversal
print(myList[4::-1])  # another list reversal

print(myList[0:3])  # 0 inclusive 3 exclusive
print(myList[0:5:2])  # jon ken sam
print(myList[0:-1])  # exclude last item

try:
    print(myList[5])
except IndexError:
    print('List out of range')

# 2d list traversal
myList2d = [[1, 2, 3], [4, 5, 6]]
for myList1d in myList2d:
    for myNum in myList1d:
        print(myNum, end=' ')
    print()

# or traverse with index
for i in range(len(myList)):
    print(str(i) + ' ' + myList[i], end=' ')

print()
print(len(myList2d))

# list concat and replication
print(myList + ['Awee'])
print(myList2d * 2)

del myList[2]  # delete element, moves up
print(myList)

# in and not in
print('Jon' in myList)
print('Abby' not in myList)

# multiple assignment
point2d = [1.5, 3]
x, y = point2d
print(x, y)

# list methods index, append, insert, remove, sort
print(myList.index('Jon'))  # find position of jon, raise ValueError
myList.sort(reverse=True)  # ascii order, uppercase first
print(myList)

myList.append('Zach')
myList.append('zoe')
myList.append('Apple')
myList.append('alex')
myList.sort(key=str.lower)  # ignore case
print(myList)

message = 'The world'
print(message[::-1])

for i in message:
    print('* * * ' + i.upper() + ' * * *')

# tuple immutable
myTuple = (5, 3, 1)
myTuple = (5)  # python thinks this is int
myTuple = (5,)  # trailing comma = tuple
print(type(myTuple))

# converting list / tuple
print(list('hello'))
print(list((1, 2, 3)))
print(tuple('hello'))
print(tuple([1, 2, 3]))

# list/dict (mutable datatype) pass as reference
copyList = myList  # pass reference
copyList = copy.copy(myList)  # shalow copy or copy.deepcopy(myList)
copyList[0] = 'NotAlex'
print(copyList)
print(myList)

# shalow copy inner list still referenced
copy2d = copy.copy(myList2d)
copy2d[0][0] = 200
copy2d[1] = 5
print(myList2d)
print(copy2d)
print()

# deep copy copy inner list too
deepcopy2d = copy.deepcopy(myList2d)
deepcopy2d[0][0] = 100
print(myList2d)
print(deepcopy2d)


def mutateList(aList):  # pass reference
    aList.append('Mutated')


mutateList(myList)
print(myList)


# take a list, comma join except last item
def joinList(aList):
    print(', '.join(aList[0:-1]) + ' and ' + aList[-1])


joinList(myList)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()
