import random

user = None

computer = random.choice(['stone','paper','scissor'])

while user == None:
    user = input('Input- Its your turn')
    if user not in ['stone','paper','scissor']:
        print('Wrong choice')
        print('Choose among stone paper scissor')
        user = None


if user == computer:
    print('Draw')
if user == 'stone':
    if computer == 'paper':
        print('computer wins')
    elif computer == 'scissor':
        print('user wins')
if user == 'paper':
    if computer == 'scissor':
        print('computer wins')
    elif computer == 'stone':
        print('user wins')
if user == 'scissor':
    if computer == 'stone':
        print('computer wins')
    elif computer == 'paper':
        print('user wins')

print('computer is {}'.format(computer))
print('user is {}'.format(user))