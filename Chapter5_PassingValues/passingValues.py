"""
Create a program that asks a user to enter a whole number between 20 and 100.
Send that number to a function that will validate the number, and if it is not
a number between 20 and 100, use a while loop to keep asking the user for a valid number.
Return the number to the main function.

hint good_number = validate(num) - use a variable to store the returned value

In addition, create three functions that determine if the number is divisible by two,
by three, and by five respectively.

Pass all of the results to a final function that displays output on the screen -
identifying whether or not the number is divisible by two, three, and five.
"""


def main():
    number = int(input("Enter a while number between 20 and 100: "))
    good_number = validate(number)

    displayResults(
        good_number,
        isDivisibleBy2(good_number),
        isDivisibleBy3(good_number),
        isDivisibleBy5(good_number)
    )


def displayResults(number, by2, by3, by5):
    if by2:
        print(f"{number} is divisible by 2")
    else:
        print(f"{number} is not divisible by 2")

    if by3:
        print(f"{number} is divisible by 3")
    else:
        print(f"{number} is not divisible by 3")

    if by5:
        print(f"{number} is divisible by 5")
    else:
        print(f"{number} is not divisible by 5")


def validate(num):
    while num < 20 or num > 100:
        print("Error: That number is not valid. Your number was not between 20 and 100. Try again. ")
        num = int(input("Enter a while number between 20 and 100: "))
    return num


def isDivisibleBy2(number):
    return number % 2 == 0


def isDivisibleBy3(number):
    return number % 3 == 0


def isDivisibleBy5(number):
    return number % 5 == 0


# ===========================================================

main()
