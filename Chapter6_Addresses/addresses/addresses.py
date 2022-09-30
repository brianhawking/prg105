"""
Write a program that gathers contact information from people. The program should
ask the user how many entries they are going to make, then ask for the Name,
phone number, and email address for each person.

You will be writing this information to a text file. Separate each value with a
comma, and make sure to include the new line character.
"""


def main():
    # open file
    address_book = open('addresses.txt', 'w')

    number_of_entries = int(input("How many people do you want to add to the file? "))

    for i in range(1, number_of_entries + 1):
        record = getRecord()
        address_book.write(record)

    address_book.close()


def getRecord():
    name = input("What is the name of the person? ")
    phone = input("What is their phone number? ")
    email = input("What is their email address? ")
    return f"{name}, {phone}, {email}\n"


# ======== Start program ========================
main()
