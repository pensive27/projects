
print("Copyright 2020. Please feel free to use the code. However, please give credit to user under the following discord username: SirNeil\n Welcome to a dice roller programme developed in Python 3.\n The programme is self explanatory. Input entry for number of dice, sides and any modifiers.\n The programme will randomly choose a number suited to the number of dice sides you chose and show the results.\nEnjoy")

import random

def roll(dice, sides, modifier):  # Define roll function
    d = 0
    while d < dice:
        rolls = random.randint(1, sides)
        d += 1
        if modifier:
            print(f"You rolled a {rolls}, which is {rolls + modifier} after applying {modifier}")
        else:
            print(f"You rolled a {rolls} without any modifiers")



def main():
    rolling = True
    while rolling:
        try:
            dice = int(input("Please enter the amount of dice you wish to roll: "))
            sides = int(input("Please enter the number of sides on your dice: "))
            modifier = int(input("Please enter any modifiers:  "))
            roll(dice, sides, modifier)

        except:
            print("please enter a value")
            continue
main()



