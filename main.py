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
        print('The currenct number is', end=' ')
        print(number)
    elif number == 0:
        print('Wow! It\'s zero!')
    number += 1