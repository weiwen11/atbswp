print(4 ** 2)  # exponent
print(15 % 10)  # mod/remainder
print(10 // 3)  # floor div
print(23 / 7)

# py3 no limit to the size of integers, limited by available memory
print(2 ** 120)

# common datatype
myInt = 5
myFloat = 1.0
myString = 'strs'

# str concat and replication
name = 'Bob' + 'by'
print(name)

name = 'Bob' * 3
print(name)

# input and casting str() int() float()
print()
print('Enter your name: ', end='')
name = input()
print('Enter your age: ', end='')
age = int(input())  # read input as string, need conversion
print('Hello ' + name + ', you will be ' + str(age + 1) + ' next year.')
print('Length of your name is ' + str(len(name)))
