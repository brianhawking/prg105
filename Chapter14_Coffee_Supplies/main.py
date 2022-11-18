"""
Using the coffee database created in the previous assignment as
your data source, generate a report showing coffee supplies by
category similar to the one below. Each category name should
appear only once and categories should be in alphabetical order.
(NOTE: Alphabetizing the products in each category is optional.)
"""

import sqlite3


class Supply:

    def __init__(self, product, category, supplier):
        self.category = category
        self.product = product
        self.supplier = supplier


def main():
    # open connection to Coffee db
    coffee_connection = sqlite3.connect("Coffee.db")

    # set up cursor
    coffee_cursor = coffee_connection.cursor()

    coffee_supplies = {}

    try:

        # Begin reading db
        select = """SELECT * FROM Coffee ORDER BY Category, Product"""
        coffee_cursor.execute(select)

        # get results
        results = coffee_cursor.fetchall()

        for row in results:
            supply = Supply(row[1], row[2], row[3])
            if row[2] in coffee_supplies:
                coffee_supplies[row[2]].append(supply)
            else:
                coffee_supplies[row[2]] = [supply]

        # Set up table headers with spacing
        print("{:>8} {:>14} {:>18}".format('Category', 'Product', 'Supplier'))
        print("{:>8} {:>18} {:>14}".format('=========', '==================', '================'))

        # Iterate over supplies, display category, and then products for that category
        for category in coffee_supplies:
            print(category)
            for item in coffee_supplies[category]:
                print("{:>8} {:<20} {:<12}".format('', item.product, item.supplier))

    except sqlite3.Error as error:
        print(error)

    coffee_connection.close()


main()
