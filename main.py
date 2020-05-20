# Create some user input data
# userInput = input('Please, type something here -->')
# print('User have typed', userInput)

# Recognize a type of data
# string = 'Some string'
# print(type(string))

# Cycle and if
# number = 0
# userNumber = int(input('Type some number: '))
# while number <= userNumber:
#     if number % 2 == 0 and number != 0:
#         print('The currencе number is', end=' ')
#         print(number)
#     elif number == 0:
#         print('Wow! It\'s zero!')
#     number += 1

# Multitudes
# семейная пара собирается в отпуск
# каждый из супругов в поездку вещи
# Max взял эти вещи
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Kate взяла эти вещи
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}
# какие вещи взяли супруги?
print(max_things | kate_things)
# найти повторяющиеся вещи
print(max_things & kate_things)
# какие вещи взял Max, но не взяла Kate
print(max_things - kate_things)
# какие вещи взяла Kate, но не взял Max
print(kate_things - max_things)

# Functions
def func(word, function):
    function(word)
    print('A simple function')

func('simple lambda funciton', lambda word: print(word.upper()))

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