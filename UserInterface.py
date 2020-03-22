# Author: Anthony Corton
# Date: 02/22/2020
# Description: Contains a class named UserInterface for an abstract game known as Xiangqi. The class contains
#              methods for introducing the player to the game, displaying game rules, and prompting for user input
#              for coordinates. A results message will be displayed at the end of the game

from XiangqiGame import XiangqiGame


class UserInterface:
    """Repesents the user interface object which will handle playing the game for the user while also providing
    helpful display outputs for command feedback and rules"""

    def __init__(self):
        """Initializes the game of Xiangqi"""
        self._player_game = XiangqiGame()


    def start(self):
        """The start function for the user interface"""
        self.introduction()
        self.game_rules()
        self.ask_user()

    def introduction(self):
        """Introduces the game and the rules to the players"""
        print("************************************************** \n" +
              "      Welcome to the game of Xiangqi ! ^_^ \n" + "************************************************** \n")

    def game_rules(self):
        """Displays a brief description of the game rules to the player"""
        print("Rules: \n" + " 1) Player red goes first \n" + " 2) Generals aren't allowed to see each other \n" +
              " 3) Generals and Advisors can not leave the castle \n" + " 4) Elephants can be blocked by diagonally"
                                                                        " adjacent pieces while Horses can be blocked by"
                                                                        " pieces located horizontally or vertically \n"
              + " 5) A player's turn will not pass till they entered a valid move, if no valid moves are possible that"
                " don't put the player's own general in check then they lose the game by stalemate \n Stalemate: "
                "Xiangqi is different than western Chess because in Xiangqi the stalemate is not a draw and is instead"
                " a loss for the player that is stalemated \n" + " 6) Locations on the board and coordinates will be "
                                                                 "entered and specified by using algebraic notation "
                                                                 "with columns a-i and rows 1-10, with row 1 being the"
                                                                 "Red side and row 10 the Black side \n")

    def ask_user(self):
        """Ask the user for coordinates to enter for the player moves"""

        while self._player_game.get_game_state() == "UNFINISHED":
            piece_starting_location = input("Please enter the location of the piece being moved: ")
            piece_moving_location = input("Please enter the location the piece will be moved to: ")
            test_move = self._player_game.make_move(piece_starting_location, piece_moving_location)

            if test_move is False:
                print("It looks like your move was invalid.  This could be because general would be left in check, "
                      "coordinates are invalid, the piece is blocked, and or there is no piece at the starting location")

            else:
                print("The move was valid")

        print("That concludes the game ")
        print("Results are the following")
        print(self._player_game.get_game_state())





