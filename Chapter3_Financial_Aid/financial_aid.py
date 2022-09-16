"""
You are writing a program to determine if a student is eligible for
financial aid for the next semester. To qualify, the student must
either be a new student or a current student with a GPA of 2.0 or higher.
Additionally, the student may not have a criminal record for drugs,
must enroll in a minimum of six credit hours of classes, and must
have a gross yearly income of less than $50,000.  You will gather
information from the student, and you will let them know if they
are eligible for financial aid or not.
"""

# Get user input
new_student = input("Are you a new student? (Enter y or n) ")

# If student is new, set gpa to 0.0. Won't matter since new_student = 'y'
if new_student == "n":
    current_gpa = float(input("What is your current gpa? "))
else:
    current_gpa = 0.0

drug_conviction = input("Have you been convicted of a drug felony? (Enter y or n) ")
num_of_credit_hours = int(input("How many credit hours are you enrolled in for next semester? "))
yearly_income = float(input("What is your gross yearly income, rounded to the nearest dollar? (No commas) "))

# Determine if the student is eligible
# Set eligible_for_aid to false
eligible_for_aid = False

if (new_student == "y" or current_gpa >= 2.0) and drug_conviction == "n" \
        and num_of_credit_hours >= 6 and yearly_income < 50000:
    eligible_for_aid = True

if eligible_for_aid:
    print("You are eligible to apply for financial aid.")
else:
    print("You are not eligible to apply for financial aid.")
