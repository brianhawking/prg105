"""
For this assignment, you will be providing the logic (plan) for the following program:

Ask the user how many students are in their class. Get the student's name and final
grade. Store the answers in a two-dimensional list, display the list, then write the
list to the grades.txt file in a comma separated format using quotes around the string
values.
"""


def main():
    # Start loop to get a valid positive integer
    try:
        num_of_students = int(input("How many students do you need to enter grades for? "))
        grades_array = getInformation(num_of_students)
        copyToFile(grades_array)
    except Exception:
        print("You did not enter a positive integer. Try again")
        main()


# Copies contents of 2D array to text file
def copyToFile(grades):
    try:
        file = open('grades.txt', 'w')
        for student in grades:
            file.write(f"'{student[0]}', '{student[1]}'\n")
        print("Grades successfully copied to 'grades.txt'")
    except Exception:
        print("There was an issue opening the grades file")


# Continue asking user for student name and grade
def getInformation(num):
    grades_array = []
    for i in range(0, num):
        name = input(f"What the name of student {i + 1}: ")
        grade = input(f"Enter the student's final grade: ")
        grades_array.append([name, grade])
    return grades_array


# ======== Start program =================================

main()
