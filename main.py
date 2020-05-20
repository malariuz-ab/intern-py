# Create some user input data
userInput = input('Please, type something here -->')
print('User have typed', userInput)

# Recognize a type of data
string = 'Some string'
print(type(string))

# Cycle and if
number = 0
userNumber = int(input('Type some number: '))
while number <= userNumber:
    if number % 2 == 0 and number != 0:
        print('The currencе number is', end=' ')
        print(number)
    elif number == 0:
        print('Wow! It\'s zero!')
    number += 1

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