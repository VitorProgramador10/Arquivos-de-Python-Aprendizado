print('Welcome to the programming world!'.center(50, '='))

ocupation = ''

name = str(input('Type your name: ')).strip()
age = int(input('Type your age: '))

while True:
    print('''Ocupation in programming world:
          [1] Begninner (Student)
          [2] Freelancer (Worker)
          [3] Employee''')
    option = int(input('Type the number corresponding to your ocupation: '))
    if option in [1, 2, 3]:
        break
    else:
        print('Invalid option! Please try again.')

if option == 1:
    ocupation = 'Begninner (Student)'
elif option == 2:
    ocupation = 'Freelancer (Worker)'
elif option == 3:
    ocupation = 'Employee'

print(f'Hello, {name}. You are {age} years old.')
print(f'You are a programmer, and your ocupation now is {ocupation}.')
print('Nice to meet you!'.center(50, '='))
