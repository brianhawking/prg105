"""
Write a program that projects yearly income, the amount saved towards retirement
each year, and total retirement savings. Assume a 3 percent raise on the starting
income each year, and a 6% yearly return on investment. You will need to ask the
user their current age, at what age they want to retire, what their current income
is, what percent of their income they save each year, and how much they currently
have in savings. You will calculate how many years until retirement, and display
the projected income, savings contribution, and total savings each year.
"""

# Constants
yearlyRaise = 0.03
ROI = 0.06

# Get user input
age = int(input("How old are you currently? "))
ageToRetire = int(input("At what age do you want to retire? "))
income = int(input("What is your yearly income? "))
savingsPercent = float(input("What percent of your income do you save? "))
totalSavings = float(input("How much money do you currently have in savings? "))

print("\nThis projection assumes a 3% raise each year and a 6% yearly return on investment.")

print("{:>8} {:>12} {:>24} {:>20}".format('Year', 'Income', 'Savings Contribution', 'Total Savings'))
for year in range(1, ageToRetire - age + 1):

    currentIncome = income * pow(1+yearlyRaise, year-1)
    contribution = currentIncome * savingsPercent / 100
    totalSavings = (totalSavings * (1+ROI)) + contribution

    print("{:>8} {:>12} {:>24} {:>20}".format(
        f"{year}",
        f"{currentIncome:,.0f}",
        f"{contribution:,.0f}",
        f"{totalSavings:,.0f}"
    ))
