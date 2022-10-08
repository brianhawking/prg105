"""
Import the data from the file. Check to see if the data is valid, if it is not
valid, indicate to the user what the bad data is. Total and average the data, and
display formatted results on the screen.
"""


def main():
    total = 0
    count = 0
    try:
        file = open('rainfall-totals.txt', 'r')
        for line in file:
            components = line.split()
            try:
                total += float(components[1])
                count += 1
                print(f"{components[0]} - {components[1]}in")
            except Exception:
                print(f"{components[0]} - {components[1]} (not a valid number)")

        if count != 0:
            print(f"\nTotal - {total:.2f}in")
            print(f"Average - {(total / count):.2f}in / month")
        else:
            print("No valid rainfalls were found.")

        file.close()

    except Exception:
        print("Error trying to open file.")


# ========= START PROGRAM =====================
main()
