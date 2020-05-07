import random

def diceroller():
    rollagain = 'yes'
    while rollagain == 'yes' or 'y':
        sides = int(input('Select a number '))
        result = random.randrange(1, sides)
        print(result)
        rollagain = input('Roll Again? ').lower()

diceroller()