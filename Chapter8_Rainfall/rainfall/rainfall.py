"""
Import the data from the file. Check to see if the data is valid, if it is not
valid, indicate to the user what the bad data is. Total and average the data, and
display formatted results on the screen.
"""


def main():
    # Initialize
    total = 0
    count = 0

    # Check to make sure the file can be opened
    try:
        file = open('rainfall-totals.txt', 'r')

        # Loop through all lines in file
        for line in file:
            # Strip the '\n' from the line before splitting
            components = line.rstrip('\n').split()

            # Try to convert rainfall to float
            # I prefer this way over "remove decimals, commas, etc." and see if
            # resulting value is a digit. I assume that happens in float() anyway
            try:
                total += float(components[1])
                count += 1
                print(f"{components[0]} - {components[1]}in")
            except Exception:
                print(f"{components[0]} - {components[1]} (not a valid number)")

        file.close()

        # Format data for user
        if count != 0:
            print(f"\nThe Total rainfall for {count} months is - {total:.2f}in")
            print(f"The Average rainfall is - {(total / count):.2f}in / month")
        else:
            print("No valid rainfalls were found.")

    except Exception:
        print("Error trying to open file.")


# ========= START PROGRAM =====================
main()
