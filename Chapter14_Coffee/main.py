"""
For this assignment, you will be providing the logic (plan) for the
following program:

Create an SQLite database with one table named Coffee. The table
should have the following fields:

ProductID INTEGER PRIMARY KEY NOT NULL
Product TEXT
Category TEXT
Supplier TEXT
Insert data into the Coffee table using the data provided in the
comma-delimited text file: coffeehouse_supplies.csvDownload
coffeehouse_supplies.csv

Tip-full-size-gold-1.png Hint: The data is comma-separated -
split on commas.

Tip-full-size-gold-1.png Hint: Refer to Inserting the Values
of Variables in section 14.5 of your book for an example of using
INSERT with variable values.

Display the number of records successfully added, or an appropriate
error message.
"""

import csv
import sqlite3


def main():

    # create database and its connection
    coffee_connection = sqlite3.connect('Coffee.db')

    # set up cursor
    coffee_cursor = coffee_connection.cursor()

    coffee_table = """CREATE TABLE IF NOT EXISTS Coffee
                    (ProductID INTEGER PRIMARY KEY NOT NULL,
                    Product TEXT,
                    Category TEXT,
                    Supplier TEXT)"""

    # execute query
    coffee_cursor.execute(coffee_table)

    # commit changes so they show up in database
    coffee_connection.commit()

    # open csv and read in data
    try:
        with open('coffeehouse_supplies.csv', 'r') as file:
            lines = csv.reader(file)

            # Iterate over lines, separate data, and insert values
            # into Coffee table
            for row in lines:
                # get values from row
                product = row[0]
                category = row[1]
                supplier = row[2].rstrip('\n')

                # insert into the coffee table
                coffee_cursor.execute("""
                        INSERT INTO Coffee (Product, Category, Supplier)
                        VALUES (?, ?, ?)""", (product, category, supplier))

                coffee_connection.commit()

                print(f"Added {product}, {category}, and {supplier} to database")

        coffee_cursor.execute("""
            SELECT count(*) FROM Coffee
        """)

        count = coffee_cursor.fetchone()
        print(f"{count[0]} rows have been added to the Coffee table.")

    except Exception:
        print("Something went wrong with opening the file")


main()
