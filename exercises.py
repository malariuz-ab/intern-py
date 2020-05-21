# Exercize
# 1
# numbers = []
#
# for i in range(3):
#     number = int(input('Type number: '))
#     numbers.append(number)
#
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# 2
# def print_sep(a, b):
#     print(a * b)
#
# print_sep('^', 40)
# print_sep('-', 50)

# 3
# def print_sep(a, b):
#     return a * b
#
# sep = print_sep('%', 50)
# text = 'This {} and this {}'.format(sep, sep)
#
# print(text)

# 4
import os
# print(os.listdir())

# 5
import sys
command = sys.argv[1]
if command == 'ping':
    print('Pong')
elif command == 'list':
    print(os.listdir())
elif command == 'name':
    name = sys.argv[2]
    print(name)