"""
You will be tracking the number of steps someone takes each day for a week.
Using a loop, ask them to enter the date and the number of steps. At the end
of the program, you will display the total number of steps taken, the day with
the most steps, and the day with the least steps. Print multiple days if they are tied.

Tip-full-size-gold-1.png Hint: Use separate loops to display the days for
the minimum and maximum values.
"""


def main():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    steps = {}
    total_steps = 0
    for day in days:
        value = int(input(f"Please enter the number of steps taken on {day}: "))
        steps[day] = value
        total_steps += value

    print(f"You walked a total of {total_steps:,} steps during the week.")
    print(f"That was an average of {(total_steps / len(days)):,.0f}")

    minimum_steps = min(steps.values())
    days_of_minimum = set()
    maximum_steps = max(steps.values())
    days_of_maximum = set()
    for key, value in steps.items():
        if value == minimum_steps:
            days_of_minimum.add(key)
        if value == maximum_steps:
            days_of_maximum.add(key)

    print(f"The minimum steps you took were {minimum_steps} on ")
    for value in days_of_minimum:
        print(f"------ {value}")

    print(f"The maximum steps you took were {maximum_steps} on ")
    for value in days_of_maximum:
        print(f"------ {value}")


# ===== START PROGRAM ===============
main()
