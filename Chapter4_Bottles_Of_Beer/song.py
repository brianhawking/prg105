"""
For this assignment, you will be providing the logic (plan) for the
following program:

Use loops to make all the lyrics of "99 bottles of beer on the wall"
print on the screen. Adjust the last two verses for correct grammar:
"""

# Starting number of beers
numberOfBottles = 99

while numberOfBottles > 0:

    # Determine whether we need to use "bottles" or "bottle" in lyrics
    if numberOfBottles == 2:
        bottleWord = "bottles"
        bottleWordMinusOne = "bottle"
    elif numberOfBottles == 1:
        bottleWord = "bottle"
        bottleWordMinusOne = "bottles"
    else:
        bottleWord = "bottles"
        bottleWordMinusOne = "bottles"

    print(f"{numberOfBottles} {bottleWord} of beer on the wall,")
    print(f"{numberOfBottles} {bottleWord} of beer,")
    print(f"Take one down, pass it around,")
    print(f"{numberOfBottles-1} {bottleWordMinusOne} of beer\n")

    numberOfBottles -= 1
