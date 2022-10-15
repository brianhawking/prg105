"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

import random
# TODO 10.2 modify Coin class to Dice
print("=" * 10, "Section 10.2 Coin class to Dice class", "=" * 10)
# modify the Coin class as indicated


class Dice:  # note class names are capitalized
    def __init__(self):
        # TODO initialize side_up to 1 (use the integer value)
        self.side_up = 1

        # TODO change toss() to roll()
    def roll(self):
        # TODO get a random value and set side_up for the 6 sides of the dice
        # Note: Think about what makes sense for dice compared to a coin toss
        self.side_up = random.randint(1, 6)
            
    def get_side_up(self):
        return self.side_up
    

def main():
    # TODO change my_coin to my_dice, my_dice_two and the appropriate class name throughout main
    my_dice = Dice()
    my_dice_two = Dice()
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())
    
    print('I am tossing the dice...')  # TODO change to dice...
    my_dice.roll()
    my_dice_two.roll()
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())


main()
