
print('------ Q 2 ------')


# ?rite a program which can compute the factorial of a given numbers.
# ?he results should be printed in a comma-separated sequence on a single line.
# ?uppose the following input is supplied to the program: 8 Then, the output should be:40320

a = int(input('ingresa num: '))
lst = []
for i in range(1, a):
    a = a * i
    lst.append(a)

print(lst)
