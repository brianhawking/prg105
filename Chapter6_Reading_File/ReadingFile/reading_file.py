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
    file = open('numeric_data.txt', 'r')

    # Initialize variables
    counter = 0
    total = 0

    # Loop through file
    for line in file:
        amount = float(line.replace(',', '').rstrip('\n'))
        print(f"{amount:,.2f}")
        counter += 1
        total += amount

    file.close()

    # Format a table to display results
    print("{:<18} {:>12}".format(
        "Total:",
        f"{total:,.2f}"
    ))
    print("{:<18} {:>12}".format(
        "Number of Entries:",
        f"{counter}"
    ))
    print("{:<18} {:>12}".format(
        "Average:",
        f"{(total / counter):,.2f}"
    ))


# ======== Start program ===============
main()
