import random

'''Function takes an input of the max number of sides for the dice and then rolls. 
Asks whether or not the user wants to roll again and gives them the option to change the max sides. 
When user decides to stop rolling, the max number of rolls will be presented as well as the roll sum.'''

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

'''Function just rolls once. 
Can be called to roll consecutively.'''

def rolldice():
    sides = int(input('Choose the maximum number of sides on the dice: '))
    result = random.randint(1, sides)
    print(result)

for i in range (0, int(input('How many times would you like to roll the dice? '))):
    rolldice()
