"""
For this assignment you will create a database that holds two
related tables: Owners and Pets. You will read in comma-delimited
text files to insert data into each of the tables. Finally, you
will display the data in a report grouped by owner.
"""

import sqlite3


# owner object created after retrieving owner and pet information
class Owner:

    # array of owner's pets
    pets = []

    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone
        self.pets = []


def main():
    # initialize owners
    owners = []

    # Set up database, connection, tables
    try:
        # create database and connection
        pets_owners_connection = sqlite3.connect("PetsOwners.db")

        # set up cursor
        pets_owners_cursor = pets_owners_connection.cursor()

        pets_owners_cursor.execute("""DROP TABLE IF EXISTS Pets""")
        pets_owners_cursor.execute("""DROP TABLE IF EXISTS Owners""")

        # create pets and owner tables
        owners_table = """CREATE TABLE IF NOT EXISTS Owners 
                        (OwnerID INTEGER PRIMARY KEY NOT NULL, OwnerName TEXT, OwnerPhone TEXT)"""

        pets_table = """CREATE TABLE IF NOT EXISTS Pets 
                        (PetID INTEGER PRIMARY KEY NOT NULL, PetName TEXT, PetType TEXT, PetBreed TEXT, OwnerID INTEGER, FOREIGN KEY (OwnerID) 
                        REFERENCES Owners(OwnerID))"""
        
        # execute table creations
        pets_owners_cursor.execute(pets_table)
        pets_owners_cursor.execute(owners_table)

        # commit changes
        pets_owners_connection.commit()

        # Get data from Owners.txt and store it in Owners Table
        try:
            input_file = open("Owners.txt", "r")

            # iterate over file
            for line in input_file:

                fields = line.rstrip("\n").split(",")
                owner_name = fields[0]
                owner_phone = fields[1]

                try:
                    insert = """INSERT INTO Owners (OwnerName, OwnerPhone)
                               VALUES (?, ?)"""

                    pets_owners_cursor.execute(insert, (owner_name, owner_phone))

                    pets_owners_connection.commit()

                except sqlite3.Error as ownersSQLError:
                    print(ownersSQLError, "inserting into owners table")

        except IOError as petsError:
            print(petsError, "opening owners.txt")

        # Get data from Pets.txt and store in Pets table
        try:
            input_file = open("Pets.txt", "r")

            # iterate over file
            for line in input_file:

                fields = line.rstrip("\n").split(",")
                pet_name = fields[0]
                pet_type = fields[1]
                pet_breed = fields[2]
                pet_ownerID = fields[3]

                try:
                    insert = """INSERT INTO Pets (PetName, PetType, PetBreed, OwnerID)
                                VALUES (?, ?, ?, ?)"""

                    pets_owners_cursor.execute(insert, (pet_name, pet_type, pet_breed, pet_ownerID))

                    pets_owners_connection.commit()

                except sqlite3.Error() as petsSQLError:
                    print(petsSQLError, "inserting into pets table")

        except IOError as error:
            print(error, "problem opening pets.txt")

        # Go through the Pets and Owners tables, create Owner object, and display owner/pet information
        try:
            # Get owners results from table
            pets_owners_cursor.execute("""SELECT * FROM Owners""")

            # get results
            owner_results = pets_owners_cursor.fetchall()

            # iterate over owners and create Owner objects
            for row in owner_results:
                owner_id = row[0]
                owner_name = row[1]
                owner_phone = row[2]

                owner = Owner(owner_id, owner_name, owner_phone)

                try:
                    # Get results from pets table
                    pets_owners_cursor.execute('SELECT * FROM Pets WHERE OwnerID = ? ORDER BY PetName', (owner_id,))

                    # get results
                    pet_results = pets_owners_cursor.fetchall()

                    # iterate over pets and add them to owners
                    for pet in pet_results:

                        pet_name = pet[1]
                        pet_type = pet[2]
                        pet_breed = pet[3]

                        pet_string = f"{pet_name} is a {pet_breed} {pet_type}"

                        owner.pets.append(pet_string)

                except sqlite3.Error as petsSQLError:
                    print(petsSQLError, "failed retrieving pets table")

                # add owner and a list of their pets to the owners array
                owners.append(owner)

        except sqlite3.Error as ownersSQLError:
            print(ownersSQLError, "failed retrieving owners table")

        displayOwners(owners)

    except sqlite3.Error as error:
        print(error, "problem opening db or creating tables")


def displayOwners(owners):
    for owner in owners:
        print(f"{owner.name}   {owner.phone}")
        for pet_string in owner.pets:
            print(f"       {pet_string}")


main()
