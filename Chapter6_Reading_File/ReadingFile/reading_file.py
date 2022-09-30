"""
For this assignment, you will be providing the logic (plan) for the
following program:

Write a program that will read numeric data from a text file line
by line using a loop. Strip the newline and convert each value to a
float, then display it. Use variables to count and total the entries.
At the end, display the total, count and average of the values.
"""


def main():

    # Open file
    file = open('numeric_data.txt', 'w')
    file.close()
