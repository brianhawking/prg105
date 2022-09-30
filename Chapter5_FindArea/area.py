"""
Create a menu function called from main that will present the user with the following menu.
This program will find the area of a shape for you.
1. Rectangle
2. Triangle
3. Square
4. Circle
5. Quit
Call a validation function from the main function to validate user input,
use a while loop to validate data. Return the validated number to the main function.
Depending on the number selected, ask the user for the appropriate measurements to
calculate the area of the specified shape (see the sample output) (Ask the user in
the menu and pass the values to the called function)
Call the appropriate function, pass the required values to the function
Return the area to the main function and print it on screen from the main function
The menu should re-display until the user selects quit. Use a while loop in the main method with a flag to accomplish this.
Create a global variable for pi and use it when calculating the area of a circle.
"""

import math

# Global variables
pi = math.pi


def main():
    selection = displayMenu()
    while selection != "5":
        while not validateSelection(selection):
            print("This is not a valid number.\n")
            selection = displayMenu()
        routeTo(selection)

        selection = displayMenu()

    print("\nThank you for playing")


def displayMenu():
    options = ["Rectangle", "Triangle", "Square", "Circle", "Quit"]
    print("This program will find the area of a shape for you.")
    for i in range(1, 6):
        print(f"{i}. {options[i - 1]}")
    selection = input("Please enter the number of your selection: ")

    return selection


# Validate functions =====================================
def validateSelection(selection):
    valid_choices = ["1", "2", "3", "4", "5"]
    for i in valid_choices:
        if i == selection:
            return True
    return False


def validatePositive(number):
    while number <= 0:
        number = float(input(f"{number} is not positive. Try again: "))
    return number


# Used to run the correct area function based on user selection =====================================
def routeTo(selection):
    if selection == "1":
        areaOfRectangle()
    elif selection == "2":
        areaOfTriangle()
    elif selection == "3":
        areaOfSquare()
    elif selection == "4":
        areaOfCircle()
    else:
        print("Something went wrong. Please try again.")


# The area functions =====================================
def areaOfRectangle():
    length = validatePositive(float(input("\nEnter the length of the rectangle in cm: ")))
    width = validatePositive(float(input("Enter the width of the rectangle in cm: ")))
    print(f"The area of the rectangle is {(length * width):.2f} square cm.\n")


def areaOfTriangle():
    base = validatePositive(float(input("\nEnter the base of the triangle in cm: ")))
    height = validatePositive(float(input("Enter the height of the triangle in cm: ")))
    print(f"The area of the triangle is {(0.5 * base * height):.2f} square cm.\n")


def areaOfSquare():
    length = validatePositive(float(input("\nEnter the length of one side of the square in cm: ")))
    print(f"The area of the square is {(length * length):.2f} square cm.\n")


def areaOfCircle():
    radius = validatePositive(float(input("\nEnter the radius of the circle in cm: ")))
    print(f"The area of the circle is {(pi * radius * radius):.2f} square cm.\n")


# ==== Start program =============================================

main()
