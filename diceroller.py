import random

def diceroller():
    rollagain = 'y'
    rolltotal = 0
    rollcount = 0
    while rollagain == 'y':
        sides = int(input('Choose the maximum number of sides on the dice: '))
        result = random.randint(1, sides)
        rolltotal = result + rolltotal
        rollcount = 1 + rollcount
        print(result)
        rollagain = input('Roll again (Y/N)? ').lower()
        if rollagain != 'y':
            print('The sum of all rolls is: ' + str(rolltotal))
            print('The number of times that you have rolled is: ' + str(rollcount))

diceroller()
