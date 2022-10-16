"""
In this programming exercise, you will create a simple trivia game for two players.
The program will work like this:

Starting with player 1, each player gets a turn at answering 5 trivia questions.
(There should be a total of 10 questions.) When a question is displayed, 4 possible
answers are also displayed. Only one of the answers is correct, and if the player
selects the correct answer, he or she earns a point.
After answers have been selected for all the questions, the program displays the number
of points earned by each player and declares the player with the highest number of points
the winner.
To create this program, write a Question class to hold the data for the trivia question.
The question class should have attributes for the following data:

A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)
The Question class should also have an appropriate __init__ method, accessors, and mutators.

The program should have a list or a dictionary containing 10 Question Objects, one for
each trivia question. Make up your own trivia question on the subject or subjects of
your choice for the objects.
"""


# Question class with question, 4 answers, and correct answer
class Question:

    def __init__(self, question, answer1, answer2, answer3, answer4, correct):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct = correct

    def isCorrect(self, answer):
        return answer == self.__correct

    def getQuestion(self):
        return self.__question

    def getAnswer1(self):
        return self.__answer1

    def getAnswer2(self):
        return self.__answer2

    def getAnswer3(self):
        return self.__answer3

    def getAnswer4(self):
        return self.__answer4

    def displayQuestion(self):
        print(f"{self.__question}")
        print(f"1. {self.__answer1}")
        print(f"2. {self.__answer2}")
        print(f"3. {self.__answer3}")
        print(f"4. {self.__answer4}")


def main():
    # questions for quiz
    questions = {
        Question("How many horns did Triceratops have?", "1", "2", "3", "4", 3),
        Question("Which time period came first?", "Jurassic", "Cretaceous", "Triassic", "20th Century", 3),
        Question("Diploducus was a", "herbivore", "carnivore", "omnivore", "pizza lover", 1),
        Question("Which dinosaur was the biggest?", "T-Rex", "Argentinosaurus", "Iguanadon", "Diploducus", 2),
        Question("Apatosaurus is also widely known by what other name?", "T-Rex", "Brontosaurus", "Triceratops",
                 "Megalodon", 2),
        Question(" What dinosaur themed book was turned into a blockbuster movie in 1993?", "Big", "Land before time",
                 "Jurassic Park", "Lost World", 3),
        Question("Which dinosaur was the first to be named?", "Brontosaurus", "Triceratops", "T-Rex", "Megalosaurus",
                 4),
        Question("Which state has Triceratops as it's state dinosaur?", "Wyoming", "Arizona", "New Mexico", "Illinois",
                 1),
        Question("A person who studies fossils and prehistoric life such as dinosaurs is known as a what?", "chemist",
                 "palaeontologists", "librarian", "barista", 2),
        Question("Dinosaurs are the ancestors of what animal?", "Reptile", "Bird", "Fish", "Beetle", 2)
    }

    # array for players score
    # index 0 -> Player 1
    # index 1 -> player 2
    players_score = [0, 0]
    current_player = 0

    # Loop through and display question and possible answers
    for question in questions:
        print(f"\nPlayer {current_player + 1}'s turn.")

        question.displayQuestion()

        answer = int(input("Choose your answer by typing in 1, 2, 3, or 4. "))

        if question.isCorrect(answer):
            players_score[current_player] += 1

        # switch player
        current_player = (current_player + 1) % 2

    # Display results
    print(f"\nPlayer 1 has a score of {players_score[0]}")
    print(f"Player 2 has a score of {players_score[1]}")

    if players_score[0] > players_score[1]:
        print(f"Player 1 is the WINNER!")
    elif players_score[0] == players_score[1]:
        print(f"Players 1 and 2 TIED")
    else:
        print(f"Player 2 is the WINNER!")


# ==== START ===========
main()
