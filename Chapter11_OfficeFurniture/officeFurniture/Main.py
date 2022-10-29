"""
For this assignment, you will demonstrate class inheritance by creating a parent
class for OfficeFurniture and a child class for Desk. You will instantiate and
display an object for each class.

In the first step, you will create a parent class for OfficeFurniture. Set the
class variables to be a category (desk, chair, filing cabinet would be example
values), material, length, width, height, and price. Include a method that
returns a string about the object. Implement the __str__ method (refer to
section 10.2 in your book for details).

In the second step create a subclass for Desk that includes location_of_drawers
(left, right, both are options) and number_drawers. Override the parents
__str__ method to include drawer location and count.
Implement each class in a separate file. Import these into your main program.
Your main program should implement and display an instance of each, the parent
class and the child class.
"""

import OfficeFurniture
import Desk


def main():
    table = OfficeFurniture.OfficeFurniture("Table", "glass", 8.5, 3.25, 3, 249.99)
    desk = Desk.Desk("wood", 6, 3, 3, 89.99, "Left", 3)

    print(table)
    print(desk)


main()
