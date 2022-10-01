"""
Use Practice 2 Program - Reading Files as a start. Modify the program to
do the following:

Request the data file name from the user.

Use a try-except statement to detect errors when opening the file.
Report any errors to the screen.

Download the file sales_error-1.txtDownload sales_error-1.txt to use as
an input file.

Use try-except to detect bad data in the input file. Report it to the
screen and skip over bad values.
Total and average the remaining good data and display results.
"""


def main():
    print("This program will total and average numbers in your data file.")
    file_name = input("Enter the name of your data file: ")

    # try to open file
    try:
        file = open(file_name, 'r')
        analyze(file)
        file.close()

    except Exception:
        print("Unable to access file:", file_name)


def analyze(file):
    # Initialize variables
    counter = 0
    total = 0

    # Loop through file
    for line in file:
        try:
            amount = float(line.rstrip('\n'))
            print(f"{amount:,.2f}")
            counter += 1
            total += amount

        except Exception:
            print(f"Line {counter + 1} with a value of {line} was invalid.")

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
