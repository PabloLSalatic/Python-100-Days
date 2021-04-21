import math
print('------ Q 1 ------')

#  Write a program which accepts a sequence of comma-separated numbers
#  from console and generate a list and a tuple which contains every number.
#  Suppose the following input is supplied to the program:

# 34, 67, 55, 33, 12, 98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# n = input('Serie de numeros:').split(',')
n = 10, 20, 30, 40  # para que no pida input
b = list(n)
print(n)
print(b)

print('------ Q 2 ------')


#    Define a class which has at least two methods:

#    getString: to get a string from console input
# printString: to print the string in upper case.

# Also please include simple test function to test the class methods.

class Mystring:
    def getString(self):
        self.string = 'hola'   # input()

    def printString(self):
        print(self.string)


x = Mystring()
x.getString()
x.printString()


print('------ Q 3 ------')

# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180

# The output of the program should be:

# 18,22,24

c = 50
h = 30
# d = input('Numeros pls: ').split(',')
d = 100, 150, 180  # para que no pida input
for i in d:
    f = ((2*c*int(i))/h)
    y = math.sqrt(f)
    print(round(y), end=',')


print('------ Q 3 ------')

# _Write a program which takes 2 digits, X, Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.*
# Note: i = 0, 1.., X-1
# j = 0, 1, ¡­Y-1. Suppose the following inputs are given to the program: 3, 5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
