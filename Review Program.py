print('Welcome to the programming world!'.center(50, '='))

occupation = ''

name = str(input('Type your name: ')).strip()
age = int(input('Type your age: '))

while True:
    print('''Occupation in programming world:
          [1] Beginner (Student)
          [2] Freelancer (Worker)
          [3] Employee''')
    option = int(input('Type the number corresponding to your occupation: '))
    if option in [1, 2, 3]:
        break
    else:
        print('Invalid option! Please try again.')

if option == 1:
    occupation = 'Beginner (Student)'
elif option == 2:
    occupation = 'Freelancer (Worker)'
elif option == 3:
    occupation = 'Employee'
print(f'Hello, {name}. You are {age} years old.')
print(f'You are a programmer, and your occupation now is {occupation}.')
print('Nice to meet you!'.center(50, '='))
