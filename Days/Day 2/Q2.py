print('------ Q 2 ------')


# ?    Define a class which has at least two methods:
# *    getString: to get a string from console input
# * printString: to print the string in upper case.
# * Also please include simple test function to test the class methods.

class Mystring:
    def getString(self):
        self.string = input('ingrese string por favor: ')

    def printString(self):
        print(self.string)


x = Mystring()
x.getString()
x.printString()
