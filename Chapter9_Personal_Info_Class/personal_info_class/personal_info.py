"""
Design a class that holds the following personal data: name, address, age, and phone number.
Write appropriate accessor and mutator methods (get and set). Write a program that creates
three instances of the class. One instance should hold your information and the other two
should hold your friends' or family members' information.  Just add information, don't
get it from the user.  Print the data from each object, make sure to format the output
for clarity and ease of reading.
"""


class PersonalInfo:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def display(self):
        print(f"{self.get_name()}, age {self.get_age()}")
        print(f"{self.get_address()}")
        print(f"{self.get_phone()}\n")


def main():
    person1 = PersonalInfo('Brian Veitch', '1344 Fountain Green, Crystal Lake, IL', 38, '815-555-1234')
    person2 = PersonalInfo('Casey Ann', '440 Lake Street, Crystal Lake, IL', 38, '815-555-5324')
    person3 = PersonalInfo('Lance Valon', '3425 Farm Road, Sycamore, IL', 45, '815-555-3243')

    person1.display()
    person2.display()
    person3.display()


# Start =========
main()
