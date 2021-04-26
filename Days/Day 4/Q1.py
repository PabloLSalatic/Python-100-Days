
# ? Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# ? Suppose the following input is supplied to the program:
# * Hello world!
# ? Then, the output should be:
# * UPPER CASE 1
# * LOWER CASE 9


my_input = input('ingresar palabras: ')
minus, mayus = 0, 0

for i in my_input:
    if ('a' <= i and i <= 'z'):
        minus += 1
    if ('A' <= i and i <= 'Z'):
        mayus += 1

print(f'UPPER CASE: {mayus} \nLOWER CASE: {minus}')
