"""
For this assignment you will write a program that keeps names and email addresses
in a dictionary as key-value pairs. The program should display a menu that lets
the user choose to lookup a person's email address, add a new name and email address,
change an existing email address, or delete an existing name and email address. The
program should pickle the dictionary and save it to a file whenever changes are made.
Each time the program starts, it should retrieve the dictionary from the file and
unpickle it. The main menu will repeat until the user chooses to QUIT.
"""

import pickle

# GLOBAL VARIABLES
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
customer_file = "customer_file.dat"


def main():

    # Intial choice so menu will run at least once
    choice = 0

    try:
        input_file = open(customer_file, 'rb')
        customer_data = pickle.load(input_file)
        input_file.close()

    except (FileNotFoundError, IOError):
        print("File not found. Adding a customer and quiting will create the file.")
        customer_data = {}

    print("Welcome to your email list manager.")

    while choice != QUIT:

        # Show user the menu, keep asking until they quit (i.e., enter 5)
        choice = displayMenu()

        # send user to approrpiate operaiton
        if choice == LOOK_UP:
            read(customer_data)
        elif choice == ADD:
            add(customer_data)
        elif choice == CHANGE:
            change(customer_data)
        elif choice == DELETE:
            delete(customer_data)
        elif choice == 5:
            print("Thanks for playing. Good bye!")


# Display CRUD menu to user
def displayMenu():

    is_valid = False

    while not is_valid:
        print("Enter your selection")
        print("   1. Look up an email by name")
        print("   2. Add a new entry.")
        print("   3. Change a person's email.")
        print("   4. Delete an entry.")
        print("   5. Quit")
        choice = input("? ")

        # Try to convert to integer. Throw exception and tell user to re-enter choice
        try:
            valid_choice = int(choice)

            # checks if user entered a valid CRUD operation
            if valid_choice != LOOK_UP and valid_choice != ADD and valid_choice != CHANGE and valid_choice != DELETE and valid_choice != QUIT:
                print("Your choice is invalid. Try again.")
            else:
                return valid_choice

        # User did not enter an integer
        except Exception:
            print("Your choice is invalid. Try again.")


# Ask user for name
# Display associated email
# Otherwise, tell them no data was found
def read(customer_data):
    name = input("Enter a name: ")
    if name in customer_data:
        print(customer_data[name])
    else:
        print("No data found. Try adding a new entry")


# Ask user for name and email
# If name doesn't exist, insert into file
def add(customer_data):
    name = input("Enter a name: ")
    email = input(f"Enter an email address for {name}: ")

    # check if user already exists
    if name in customer_data:
        print(f"{name} already exists.")
    else:
        # add to dictionary
        customer_data[name] = email

        # Save to file
        save(customer_data)

        # Show confirmation
        print(f"{name} has been added to the email {email}")


# ask user for name
# If it exists, display email and ask if they want to change it
# If so, edit the dictionary and save it to file
def change(customer_data):
    name = input("Enter a name: ")
    if name in customer_data:
        choice = input(f"Current email for {name} is {customer_data[name]}. Do you want to change it? (y/n): ")
        if choice == "y" or choice == "Y":
            customer_data[name] = input(f"Enter the new email for {name}: ")
            save(customer_data)
            print(f"The email for {name} is now {customer_data[name]}")
    else:
        print("No data found. Try adding a new entry")


# Ask user for name
# If name exists, display email and ask if they want to delete it.
# Show confirmation of user's choice
def delete(customer_data):
    name = input("Enter a name: ")
    if name in customer_data:
        choice = input(f"Current email for {name} is {customer_data[name]}. Do you want to delete it? (y/n): ")
        if choice == "y" or choice == "Y":
            del customer_data[name]
            save(customer_data)
            print(f"{name} has been removed.")
    else:
        print("No data found. Try adding a new entry")



# Save dictionary to file
def save(customer_data):

    try:
        input_file = open(customer_file, 'wb')
        pickle.dump(customer_data, input_file)
        print("The file has been updated with your changes.")

    except Exception:
        print(f"There was a problem saving to {customer_file}")


# === START =====
main()
