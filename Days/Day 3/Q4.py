
# ?Write a program that accepts a sentence and calculate the number of letters and digits.

# ?Suppose the following input is supplied to the program:
# *hello world! 123

# ?Then, the output should be:
# *LETTERS 10
# *DIGITS 3

my_input = input('ingresar palabra y digitos: ')
letter, digit = 0, 0

for i in my_input:
    if ('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z'):
        letter += 1
    if '0' <= i and i <= '9':
        digit += 1

print(f'LETTERS: {letter} \n DIGITS: {digit}')
