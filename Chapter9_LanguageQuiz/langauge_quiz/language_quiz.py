"""
Create a dictionary based on the language of your choice with the numbers
from 1-10 paired with the numbers from 1-10 in English. Create a quiz
based on this dictionary. Display the number in a foreign language and
ask for the number in English. Score the test and give the user a letter grade.
"""


def main():
    language_translations = {
        'eins': 'one',
        'zwei': 'two',
        'drei': 'three',
        'vier': 'four',
        'funf': 'five',
        'sechs': 'six',
        'sieben': 'seven',
        'acht': 'eight',
        'neun': 'nine',
        'zehn': 'ten'
    }

    grades = {
        '10': 'A',
        '9': 'A',
        '8': 'B',
        '7': 'C',
        '6': 'D',
        '5': 'F',
    }

    score = 0

    print("Enter the number in English which corresponds to the number in German.")

    for key, value in language_translations.items():
        answer = input(f"What is the equivalent of {key}: ")
        if answer == value:
            score += 1
            print("Correct")
        else:
            print(f"Incorrect. The correct answer is {value}")

    print(f"Your final score is {score}/{len(language_translations)}")
    print(f"{grades.get(str(score), 'F')}")


# ======== START =============
main()
