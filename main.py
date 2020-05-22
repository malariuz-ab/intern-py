# Internal types
string = 'Simple string'
print(type(string))
int = 23
print(type(int))
float = 45.56
print(type(float))
list = [2, 3, 4, 4]
print(type(list))
korsage = (2, 3, 4)
print(type(korsage))
dictionary = {'one':1, 'two':2}
print(type(dictionary))
multy = {2, 3, 4}
print(type(multy))

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

# User is typing something
userInput = input('Please, type something here: ')
print('User have typed', userInput)

# Cycle and if
number = 0
userNumber = 1000 # int(input('Type some number: '))
while number <= userNumber:
    if number % 2 == 0 and number != 0:
        print('The currencе number is', end=' ')
        print(number)
    elif number == 0:
        print('Wow! It\'s zero!')
    elif number == 1000:
        pass # we can use: continue, break
    number += 1
else:
    pass

# Functions
def func(word, function):
    function(word)
    print('A simple function')

func('simple lambda funciton', lambda word: print(word.upper()))

# Moduls
# from modules.module import foo
# print(foo)
# from Doctors.main import get_doctors
# get_doctors()
import os, sys
print(os.path)
print(sys.path)

# Make directory and OS + interpretater of Python
import os, sys
# name = sys.platform
# for i in range(1, 6):
#     new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
#     os.mkdir(new_path)

# Open files and if a file doesn't exist it will be created
# The simple opening with close()
file = open('simplefile.txt', 'w')
file.write('First line\n')
file.write('Second line\n')
file.writelines(['One\n', 'Two\n'])
file.close()
# The opening with WITH construction
with open('simplefile.txt', 'r') as file:
    for line in file:
        print(line.replace('\n', ''))

# Encode & decode, bytes & strings
s = 'Hello world и я'
sb = s.encode('utf-8')
print(sb)
print(type(sb))
s = sb.decode('utf-8')
print(s)
print(type(s))

# Files & bytes
with open('simplefile.txt', 'wb') as f:
    f.write(b'These are bytes')
with open('simplefile.txt', 'rb') as f:
    print(f.read())
with open('simplefile.txt', 'r', encoding='utf-8') as f: # here we open file by forcing encoding
    pass

# Generators
# Structure (on a list generator) [what we will write in a list, cycle (for ... in ...), if ...]
import random
numbers = [1, 2, 3, 4, 5, 6, -1, -2, -3]
result = [number for number in numbers if number > 0] # for lists
print(result)
pairs = [(1, 'b'), (2, 'b'), (3, 'c')]
result = {pair[0]: pair[1] for pair in pairs}
print(result)
randomN = [random.randint(1, 100) for i in range(10)] # a focus
print(randomN)

# Exeptions
a = 3
b = '4'
try:
    print(a + b)
except Exception as e:
    print('Error: ', e)
else:
    print('Everything is awesome! Any error isnt entertained')
finally:
    print('I\'m always run')
# We can generate exeption
print('Begin')
#raise Exception('Something goes wrong')
print('End')

# Insert verbials
a = 2
b =3
string = f'<div>{a}</div>{b}'