"""
For this assignment, you will be providing the logic (plan) for the following program:

Create a program that helps someone create a budget. It should ask the user for monthly income and
for each of the following expenses:
Housing
Food
Transportation
Phone
Utilities
Clothing
The program should get input from the user and convert each of the inputs to floats.
The program should calculate and display the income percentage of each budget item.
The program should also tell the user how much money they have left after subtracting the budgeted items from the income.
"""

print(f"Please enter your monthly expenses to determine their monthly percentages.\n")

# Get user's monthly income and monthly expenses

monthly_income = float(input("How much is your total monthly income? "))
housing_expense = float(input("How much do you spend on housing (rent/mortgage) each month? "))
food_expense = float(input("How much do you spend on food, restaurants, etc. each month? "))
transportation_expense = float(input("How much do you spend on transportation each month? "))
phone_expense = float(input("How much do you spend on your phone each month? "))
utilities_expense = float(input("How much do you spend on utilities (electric, gas, sewage, etc.) each month? "))
clothing_expense = float(input("How much do you spend on clothing (clothing, accessories, etc.) each month? "))


# Calculate percentages and display output
print("\n")
print(f"Housing takes up {(housing_expense / monthly_income):.2%} of your monthly income.")
print(f"Food takes up {(food_expense / monthly_income):.2%} of your monthly income.")
print(f"Transportation takes up {(transportation_expense / monthly_income):.2%} of your monthly income.")
print(f"Your phone takes up {(phone_expense / monthly_income):.2%} of your monthly income.")
print(f"Utilities takes up {(utilities_expense / monthly_income):.2%} of your monthly income.")
print(f"Clothing takes up {(clothing_expense / monthly_income):.2%} of your monthly income.")

remaining_money = monthly_income - \
                  (housing_expense + food_expense + transportation_expense + phone_expense + utilities_expense + clothing_expense)

print("\n")
print(f"You have ${remaining_money:.2f} left from your income after paying these monthly expenses.")
