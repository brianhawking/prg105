"""
You will create two classes, a parent class and a child class, in one file. You will import that file into a separate file holding your program code.

File 1:

Write an Employee class that keeps data attributes for the following pieces of information:

Employee name
Employee number
Next, write a class named ProductionWorker that is a subclass of the Employee class. The ProductionWorker class should keep data attributes for the following information

Shift numbered (an integer, such as 1, 2, or 3)
Hourly pay rate
The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the night shift is shift 2.

Write the appropriate accessor and mutator methods (get and set) for each class.

File 2:

Once you have written the classes, write a program that creates an object of the ProductionWorker class and prompts the user to enter data for each of the object’s data attributes. Store the data in the object and then use the object’s accessor methods to retrieve it and display it on the screen.
"""

import Employee


def main():

    # Get Employee's (specifically production worker) information
    print("Enter Employee Information")
    name = input("Name: ")
    number = input("Employee Number: ")
    shift = int(input("Shift (1 = day, 2 = night): "))
    hourly_rate = float(input("Hourly pay rate:  "))

    # Instantiate worker
    production_worker = Employee.ProductionWorker(name, number, shift, hourly_rate)

    # Display to screen
    print("\nEmployee Information")
    print("-------------------------")
    print(f"Employee: {production_worker.get_employee_number()} {production_worker.get_employee_name()}")
    print(f"     Shift: {production_worker.get_shift_description()}")
    print(f"     Pay Rate: ${production_worker.get_hourly_rate():.2f}")


# ======= START =====
main()
