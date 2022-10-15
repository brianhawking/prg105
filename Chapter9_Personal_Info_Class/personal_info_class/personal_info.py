"""
Design a class that holds the following personal data: name, address, age, and phone number.
Write appropriate accessor and mutator methods (get and set). Write a program that creates
three instances of the class. One instance should hold your information and the other two
should hold your friends' or family members' information.  Just add information, don't
get it from the user.  Print the data from each object, make sure to format the output
for clarity and ease of reading.
"""


class PersonalInfo:
    def __init__(self):
        self.name = None
        self.address = None
        self.age = None
        self.phone = None

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone

    def display(self):
        print(f"{self.get_name()}, age {self.get_age()}")
        print(f"{self.get_address()}")
        print(f"{self.get_phone()}")

def main():
    person1 = PersonalInfo()
    
