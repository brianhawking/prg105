import random
import math

"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 5.2 - calling an existing function
print("=" * 10, "Section 5.2 call an existing function", "=" * 10)


# Beneath the following function, write the code to call it
# Remove the """ """ before testing
# Note: Python requires two blank lines before a function definition


def hello():
    print("Hello Sweetie!")


# Write the code to call the hello function on the next line
hello()

# TODO 5.2 - creating and calling a void function
print("=" * 10, "Section 5.2 create and call a void function", "=" * 10)


# Write a function called joke that prints a joke on the screen
# Call the function

def joke():
    print("What do you get if you cross a dinosaur with a pig? Jurassic Pork!")


joke()

# TODO 5.3 designing a program in functions
print("=" * 10, "Section 5.3 design a program using functions", "=" * 10)


# Create a main function that will call separate functions that
# print each line in a knock-knock joke. Make sure to call main
# as the last line of your code.


def main():
    input("Press enter to see each part of the knock knock joke. Ready? Press enter.")
    knockknock()

    input()
    whosThere()

    input()
    answer()

    input()
    answerWho()

    input()
    punchline()


def knockknock():
    print("Knock knock")


def whosThere():
    print("Who's there?")


def answer():
    print("Nobel")


def answerWho():
    print("Nobel who?")


def punchline():
    print("Nobel... that's why I knocked.")


main()

# TODO 5.4 local variables
print("=" * 10, "Section 5.4 using local variables", "=" * 10)


# 1) Write a program with a main2 function. In main2, define a variable
#    called name and assign a name to it using a string, then print hello
#    and the name variable. Have main2 call a second function get_name().
# 2) In the get_name function, ask the user for their name,
#    then greet them using a print statement.
# 3) Call the main2 function.
# Note - you would not normally have more than one main function
# in a program, we are just adding the number after main to allow
# us to write multiple short practice programs in a single file.


def main2():
    name = "Brian"
    print(f"Hello {name}")

    get_name()


def get_name():
    name = input("What is your name? ")
    print(f"Hello {name}")


main2()

# TODO 5.5 passing arguments to Functions
print("=" * 10, "Section 5.5 passing arguments", "=" * 10)


# Complete the code below to pass the my_number variable value from
# main3() into square() using a parameter name of value.
# Remove the """ """ before testing


def main3():
    my_number = 7
    square(my_number)


def square(value):
    squared_value = value * value
    print(squared_value)


main3()

# TODO 5.5 passing multiple arguments
print("=" * 10, "Section 5.5 passing multiple arguments", "=" * 10)


# Complete the code below to pass the variables from main4() into
# parameters for add(). Look at the code to determine the correct
# variable / parameter names. Remove the """ """

def main4():
    num_one = 5
    num_two = 7
    add(num_one, num_two)


def add(one, two):
    total = one + two
    print(total)


main4()

# TODO 5.6-5.7 value returning functions
print("=" * 10, "Section 5.6-5.7 value returning functions", "=" * 10)
# Add a statement importing the random library at the top of this file: import random
# Add a global constant PI with a value of 3.14 before the main5() function definition

PI = 3.14


def main5():
    r = random.randint(1, 10)
    r2 = r * r
    area(r2)


def area(radius_squared):
    my_area = PI * radius_squared
    print(f"{my_area: ,.2f}")


main5()

# TODO 5.8 value returning functions
print("=" * 10, "Section 5.8 value returning functions", "=" * 10)


# Complete the following program, remove the """  """ before testing


def main6():
    print("This program will calculate your BMI")
    height = float(input("What is your height in inches?  "))
    weight = float(input("What is your weight in pounds?  "))

    answer1 = bmi(weight, height)

    # TODO print the variable answer, make sure to format it to 1 decimal place
    print(f"Your BMI is {answer1:.1f}")


def bmi(weight_pounds, height_inches):
    # BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
    patient_bmi = (weight_pounds / (height_inches * height_inches)) * 703

    return patient_bmi


main6()

# TODO 5.9 the math module
print("=" * 10, "Section 5.9 use the math module", "=" * 10)
# Add the import math statement at the top of this file: import math
# Write a statement that uses the ceil function on the following variable
# Display the result
number_to_round = 4.243


def printCeiling(number):
    ceiling = math.ceil(number)
    print(f"{ceiling}")


printCeiling(number_to_round)
