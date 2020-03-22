
from XiangqiGame import XiangqiGame

class UserInterface:

    def __init__(self):
        """Initializes the game of Xiangqi"""
        player_game = XiangqiGame()


    def start(self):
        """The start function for the user interface"""
        self.introduction()


    def introduction(self):
        """Introduces the game and the rules to the players"""
        print("Welcome to the game of Xiangqi ! ^_^ \n" + "The red piece will start first, player's turns will not end"
                                                      " till they entered a valid move and if a player has no valid"
                                                      "moves that player loses by stalemate")

