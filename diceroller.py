import random

def diceroller():
    rollagain = 'y'
    rolltotal = 0
    rollcount = 0
    while rollagain == 'y':
        sides = int(input('Choose the maximum sides of the dice: '))
        result = random.randrange(1, sides)
        rolltotal = result + rolltotal
        rollcount = 1 + rollcount
        print(result)
        rollagain = input('Roll again (Y/N)? ').lower()
        if rollagain != 'y':
            print('The sum of all rolls is: ' + str(rolltotal))
            print('You have rolled ' + str(rollcount) + ' times.')
diceroller()
