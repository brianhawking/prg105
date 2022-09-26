"""
Create a program that presents the user with five choices. The topic
could be game characters, food, car packages, anything you are interested in.
You will put a menu on the screen, ask the user to enter the number or letter
of their choice, and then call the corresponding function to give the user
more information.
"""


# Displays a list of games for the user to choose.
def displayOptions():

    games = ["Chess", "Catan", "Rocket League", "Skyrim", "Ticket To Ride"]

    print("Please select an option below to see a description of that game.")

    # Cycle through array of games to display the option
    for i in range(0, 5):
        print(f"{i + 1}: {games[i]}")

    selection = int(input("Please enter the number of your choice: "))

    # Continue to ask the question until they enter a valid entry
    while selection <= 0 or selection > 5:
        selection = int(input("Error: Please select an option between 1 and 5. I select: "))

    routeTo(games[selection - 1])


def routeTo(game):
    print("")
    if game == "Chess":
        chess()
    elif game == "Catan":
        catan()
    elif game == "Rocket League":
        rocketLeague()
    elif game == "Skyrim":
        skyrim()
    elif game == "Ticket To Ride":
        ticketToRide()
    else:
        print("You did not enter a valid number")


def chess():
    print("Chess is an abstract strategy game and involves no hidden information. \n"
          "It is played on a square chessboard with 64 squares arranged in an \n"
          "eight-by-eight grid. At the start, each player (one controlling the \n"
          "white pieces, the other controlling the black pieces) controls sixteen \n"
          "pieces: one king, one queen, two rooks, two bishops, two knights, and \n"
          " eight pawns. The object of the game is to checkmate the opponent's king, \n"
          "whereby the king is under immediate attack (in check) and there is no \n"
          "way for it to escape.")


def catan():
    print("Catan, previously known as The Settlers of Catan or simply Settlers, is a \n"
          "multiplayer board game designed by Klaus Teuber. It was first published in \n"
          "1995 in Germany by Franckh-Kosmos Verlag (Kosmos) as Die Siedler von Catan. \n"
          "Players take on the roles of settlers, each attempting to build and develop \n"
          "holdings while trading and acquiring resources. Players gain victory points \n"
          "as their settlements grow; the first to reach a set number of victory points, \n"
          "typically 10, wins. ")


def rocketLeague():
    print("Described as soccer, but with rocket-powered cars, Rocket League has up to eight \n"
          "players assigned to each of the two teams, using rocket-powered vehicles to hit \n"
          "a ball into their opponent's goal and score points over the course of a match. \n"
          "The game includes single-player and multiplayer modes that can be played both \n"
          "locally and online, including cross-platform play between all versions. Later \n"
          "updates for the game enabled the ability to modify core rules and added new game \n"
          "modes, including ones based on ice hockey and basketball.")


def skyrim():
    print("The Elder Scrolls V: Skyrim is an action role-playing video game developed by \n"
          "Bethesda Game Studios and published by Bethesda Softworks. It is the fifth main \n"
          "installment in the Elder Scrolls series, following 2006's The Elder Scrolls IV: Oblivion,\n"
          "and was released worldwide for Microsoft Windows, PlayStation 3, and Xbox 360 on November 11, \n"
          "2011. "
          "\n\nThe game is set 200 years after the events of Oblivion, and takes place in Skyrim, \n"
          "the northernmost province of Tamriel. Its main story focuses on the player's character, \n"
          "the Dragonborn, on their quest to defeat Alduin the World-Eater, a dragon who is \n"
          "prophesied to destroy the world. Over the course of the game, the player completes \n"
          "quests and develops the character by improving skills. The game continues the open-world \n"
          "tradition of its predecessors by allowing the player to travel anywhere in the game world \n"
          "at any time, and to ignore or postpone the main storyline indefinitely.")


def ticketToRide():
    print("With elegantly simple gameplay, Ticket to Ride can be learned in under 15 minutes. \n"
          "Players collect cards of various types of train cars they then use to claim railway\n"
          " routes in North America. The longer the routes, the more points they earn.\n"
          " Additional points come to those who fulfill Destination Tickets – goal cards that \n"
          "connect distant cities; and to the player who builds the longest continuous route.")


# =======================================================


displayOptions()
