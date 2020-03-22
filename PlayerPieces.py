# Author: Anthony Corton
# Date: 02/22/2020
# Description: Contains a class named PlayerPiece for an abstract game known as Xiangqi. The class contains
#              methods for getting team, piece, legal move, and setting and getting piece location. The 7 distinct
#              game board pieces all inherit from the PlayerPiece class and are included in this file



class PlayerPiece:
    """Represent's an object of the one of the player's pieces in the game (chariot, elephant, general, etc)"""

    def __init__(self, team, piece_name, piece_location):
        """Return's a player piece object and takes as a parameter the team the object belong's too (red or black)"""
        self._team = team
        self._piece_name = piece_name
        self._piece_location = piece_location

    def get_team(self):
        """Returns' the pieces team it belongs too"""
        return self._team

    def get_piece(self):
        """Returns the piece name"""
        return self._piece_name

    def get_legal_move(self, original, from_location, to_location):
        """Takes as a parameter a board object and returns a list of legal moves allowed for the piece"""

    def set_location(self, location):
        """Sets the new location of the piece"""
        self._piece_location = location

    def get_location(self):
        """Returns the location of the piece"""
        return self._piece_location

class King(PlayerPiece):
    """Represents a General piece on the game board. The class inherits from the PLayerPiece class with its own
    unique get_legal_move function"""

    def get_legal_move(self, game_board, from_location, to_location):
        """Takes as a parameter a board and returns a list of legal moves for the king piece"""

        if self.get_team() == "red" and (to_location[0] > 2 or to_location[0] < 0):         # out of bounds for red
            return False
        if self.get_team() == "red" and (to_location[1] > 5 or to_location[1] < 3):
            return False

        if self.get_team() == "black" and (to_location[0] < 7 or to_location[0] > 9):       # out of bounds for black
            return False
        if self.get_team() == "black" and (to_location[1] > 5 or to_location[1] < 3):
            return False


        if self.get_team() == "red":
            if from_location[0] == to_location[0] and from_location[1] + 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] == to_location[0] and from_location[1] - 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] + 1 == to_location[0] and from_location[1] == to_location[1]:   # for moving up in row
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] == to_location[1]:  # for moving up in row
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True


        elif self.get_team() == "black":
            if from_location[0] == to_location[0] and from_location[1] + 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] == to_location[0] and from_location[1] - 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] + 1 == to_location[0] and from_location[1] == to_location[1]:   # for moving up in row
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] == to_location[1]:  # for moving up in row
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

        return False
class Guard(PlayerPiece):
    """Represents a guard piece on the game board. The class inherits from the PLayerPiece class with its own
    unique get_legal_move function"""

    def get_legal_move(self, game_board, from_location, to_location):
        """Takes as a parameter a board and returns a list of legal moves for the guard piece"""

        if self.get_team() == "red" and (to_location[0] > 2 or to_location[0] < 0):  # out of bounds for red
            return False
        if self.get_team() == "red" and (to_location[1] > 5 or to_location[1] < 3):
            return False

        if self.get_team() == "black" and (to_location[0] < 7 or to_location[0] > 9):  # out of bounds for black
            return False
        if self.get_team() == "black" and (to_location[1] > 5 or to_location[1] < 3):
            return False


        if self.get_team() == "red":
            if from_location[0] + 1 == to_location[0] and from_location[1] - 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] + 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] + 1 == to_location[0] and from_location[1] + 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] - 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

        elif self.get_team() == "black":
            if from_location[0] + 1 == to_location[0] and from_location[1] - 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][
                    to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] + 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][
                    to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] + 1 == to_location[0] and from_location[1] + 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][
                    to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] - 1 == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][
                    to_location[1]].get_team() == "red":
                    return True

        return False

class Elephant(PlayerPiece):
    """Represents a Elephant piece on the game board. The class inherits from the PLayerPiece class with its own
    unique get_legal_move function"""

    def get_legal_move(self, game_board, from_location, to_location):
        """Takes as a parameter a board and returns a list of legal moves for the elephant piece"""
        if self.get_team() == "red" and (to_location[0] > 4 or to_location[0] < 0):  # out of bounds for red
            return False

        if self.get_team() == "black" and (to_location[0] < 5 or to_location[0] > 9):  # out of bounds for black
            return False

        if self.get_team() == "red":
            if from_location[0] + 2 == to_location[0] and from_location[1] - 2 == to_location[1]: # up to the left
                if game_board[from_location[0] + 1][from_location[1] - 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] + 2 == to_location[0] and from_location[1] + 2 == to_location[1]: # up to the right
                if game_board[from_location[0] + 1][from_location[1] + 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 2 == to_location[0] and from_location[1] - 2 == to_location[1]:  # back to the left
                if game_board[from_location[0] - 1][from_location[1] - 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 2 == to_location[0] and from_location[1] + 2 == to_location[1]:  # back to the right
                if game_board[from_location[0] - 1][from_location[1] + 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][
                    to_location[1]].get_team() == "black":
                    return True

        elif self.get_team() == "black":
            if from_location[0] + 2 == to_location[0] and from_location[1] - 2 == to_location[1]: # up to the left
                if game_board[from_location[0] + 1][from_location[1] - 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] + 2 == to_location[0] and from_location[1] + 2 == to_location[1]: # up to the right
                if game_board[from_location[0] + 1][from_location[1] + 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 2 == to_location[0] and from_location[1] - 2 == to_location[1]:  # back to the left
                if game_board[from_location[0] - 1][from_location[1] - 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 2 == to_location[0] and from_location[1] + 2 == to_location[1]:  # back to the right
                if game_board[from_location[0] - 1][from_location[1] + 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

        return False

class Horse(PlayerPiece):
    """Represents a horse piece on the game board. The class inherits from the PLayerPiece class with its own
    unique get_legal_move function"""


    def get_legal_move(self, game_board, from_location, to_location):
        """Takes as a parameter a board and returns a list of legal moves for the horse piece"""

        if to_location[0] > 9 or to_location[0] < 0:  # out of bounds of the board for both red and black horse
            return False

        if to_location[1] > 8 or to_location[1] < 0:
            return False

        if self.get_team() == "red":
            if from_location[0] + 2 == to_location[0] and from_location[1] - 1 == to_location[1]: # up to the left
                if game_board[from_location[0] + 1][from_location[1]] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] + 2 == to_location[0] and from_location[1] + 1 == to_location[1]: # up to the right
                if game_board[from_location[0] + 1][from_location[1]] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 2 == to_location[0] and from_location[1] - 1 == to_location[1]:  # back to the left
                if game_board[from_location[0] - 1][from_location[1]] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 2 == to_location[0] and from_location[1] + 1 == to_location[1]:  # back to the right
                if game_board[from_location[0] - 1][from_location[1]] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] + 2 == to_location[1]:  # to the right and back
                if game_board[from_location[0]][from_location[1] + 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] + 1 == to_location[0] and from_location[1] + 2 == to_location[1]:  # to the right and up
                if game_board[from_location[0]][from_location[1] + 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] - 2 == to_location[1]:  # to the left and back
                if game_board[from_location[0]][from_location[1] - 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] + 1 == to_location[0] and from_location[1] - 2 == to_location[1]:  # to the left and up
                if game_board[from_location[0]][from_location[1] - 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

        if self.get_team() == "black":
            if from_location[0] + 2 == to_location[0] and from_location[1] - 1 == to_location[1]:  # up to the left
                if game_board[from_location[0] + 1][from_location[1]] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] + 2 == to_location[0] and from_location[1] + 1 == to_location[1]:  # up to the right
                if game_board[from_location[0] + 1][from_location[1]] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 2 == to_location[0] and from_location[1] - 1 == to_location[1]:  # back to the left
                if game_board[from_location[0] - 1][from_location[1]] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 2 == to_location[0] and from_location[1] + 1 == to_location[1]:  # back to the right
                if game_board[from_location[0] - 1][from_location[1]] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] + 2 == to_location[1]:  # to the right and back
                if game_board[from_location[0]][from_location[1] + 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] + 1 == to_location[0] and from_location[1] + 2 == to_location[1]:  # to the right and up
                if game_board[from_location[0]][from_location[1] + 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] - 1 == to_location[0] and from_location[1] - 2 == to_location[1]:  # to the left and back
                if game_board[from_location[0]][from_location[1] - 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] + 1 == to_location[0] and from_location[1] - 2 == to_location[1]:  # to the left and up
                if game_board[from_location[0]][from_location[1] - 1] != "":
                    return False
                elif game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

        return False

class Chariot(PlayerPiece):
    """Represents a chariot piece on the game board. The class inherits from the PLayerPiece class with its own
    unique get_legal_move function"""

    def get_legal_move(self, game_board, from_location, to_location):
        """Takes as a parameter a board and returns a list of legal moves for the chariot piece"""

        if (to_location[0] > 9 or to_location[0] < 0) or (to_location[1] > 8 or to_location[1] < 0):
            return False

        if self.get_team() == "red":
            if from_location[0] == to_location[0] and to_location[1] > from_location[1]:  # if moving to the right same row
                counter = 1
                while game_board[from_location[0]][from_location[1] + counter] == "":
                    if from_location[1] + counter == to_location[1] and (game_board[from_location[0]][from_location[1] + counter] == ""):
                        return True
                    counter += 1

                if from_location[1] + counter == to_location[1] and game_board[from_location[0]][from_location[1] + counter].get_team() == "black":
                    return True

            elif from_location[0] == to_location[0] and to_location[1] < from_location[1]:  # if moving to the left same row
                counter = 1
                while game_board[from_location[0]][from_location[1] - counter] == "":
                    if from_location[1] - counter == to_location[1] and (game_board[from_location[0]][from_location[1] - counter] == ""):
                        return True
                    counter += 1

                if from_location[1] - counter == to_location[1] and game_board[from_location[0]][from_location[1] - counter].get_team() == "black":
                    return True

            if from_location[1] == to_location[1] and to_location[0] > from_location[0]:  # if moving to the up same column
                counter = 1
                while game_board[from_location[0] + counter][from_location[1]] == "":
                    if from_location[0] + counter == to_location[0] and (game_board[from_location[0] + counter][from_location[1]] == ""):
                        return True
                    counter += 1

                if from_location[0] + counter == to_location[0] and game_board[from_location[0] + counter][from_location[1]].get_team() == "black":
                    return True

            if from_location[1] == to_location[1] and to_location[0] < from_location[0]:  # if moving down the same column
                counter = 1
                while game_board[from_location[0] - counter][from_location[1]] == "":
                    if from_location[0] - counter == to_location[0] and (game_board[from_location[0] - counter][from_location[1]] == ""):
                        return True
                    counter += 1

                if from_location[0] - counter == to_location[0] and game_board[from_location[0] - counter][from_location[1]].get_team() == "black":
                    return True

        if self.get_team() == "black":
            if from_location[0] == to_location[0] and to_location[1] > from_location[1]:  # if moving to the right same row
                counter = 1
                while game_board[from_location[0]][from_location[1] + counter] == "":
                    if from_location[1] + counter == to_location[1] and (game_board[from_location[0]][from_location[1] + counter] == ""):
                        return True
                    counter += 1

                if from_location[1] + counter == to_location[1] and game_board[from_location[0]][from_location[1] + counter].get_team() == "red":
                    return True

            elif from_location[0] == to_location[0] and to_location[1] < from_location[1]:  # if moving to the left same row
                counter = 1
                while game_board[from_location[0]][from_location[1] - counter] == "":
                    if from_location[1] - counter == to_location[1] and (game_board[from_location[0]][from_location[1] - counter] == ""):
                        return True
                    counter += 1

                if from_location[1] - counter == to_location[1] and game_board[from_location[0]][from_location[1] - counter].get_team() == "red":
                    return True

            if from_location[1] == to_location[1] and to_location[0] > from_location[0]:  # if moving to the up same column
                counter = 1
                while game_board[from_location[0] + counter][from_location[1]] == "":
                    if from_location[0] + counter == to_location[0] and (game_board[from_location[0] + counter][from_location[1]] == ""):
                        return True
                    counter += 1

                if from_location[0] + counter == to_location[0] and game_board[from_location[0] + counter][from_location[1]].get_team() == "red":
                    return True

            if from_location[1] == to_location[1] and to_location[0] < from_location[0]:  # if moving down the same column
                counter = 1
                while game_board[from_location[0] - counter][from_location[1]] == "":
                    if from_location[0] - counter == to_location[0] and (game_board[from_location[0] - counter][from_location[1]] == ""):
                        return True
                    counter += 1

                if from_location[0] - counter == to_location[0] and game_board[from_location[0] - counter][from_location[1]].get_team() == "red":
                    return True

        return False
class Cannon(PlayerPiece):
    """Represents a cannon piece on the game board. The class inherits from the PLayerPiece class with its own
    unique get_legal_move function"""

    def get_legal_move(self, game_board, from_location, to_location):
        """Takes as a parameter a board and returns a list of legal moves for the cannon piece"""
        if (to_location[0] > 9 or to_location[0] < 0) or (to_location[1] > 8 or to_location[1] < 0):
            return False

        if self.get_team() == "red":
            if from_location[0] == to_location[0] and to_location[1] > from_location[1]:  # if moving to the right same row
                counter = 1
                while game_board[from_location[0]][from_location[1] + counter] == "":
                    if from_location[1] + counter == to_location[1] and (game_board[from_location[0]][from_location[1] + counter] == ""):
                        return True
                    counter += 1


                if from_location[1] + counter != to_location[1] and game_board[from_location[0]][from_location[1] + counter] != "":
                    counter += 1
                    while game_board[from_location[0]][from_location[1] + counter] == "" and from_location[1] + counter < 8:
                        counter += 1

                    if game_board[from_location[0]][from_location[1] + counter] == "":
                        return False

                    if game_board[from_location[0]][from_location[1] + counter].get_team() == "black":
                        if from_location[1] + counter == to_location[1]:
                            return True

            elif from_location[0] == to_location[0] and to_location[1] < from_location[1]:  # if moving to the left same row
                counter = 1
                while game_board[from_location[0]][from_location[1] - counter] == "":
                    if from_location[1] - counter == to_location[1] and (game_board[from_location[0]][from_location[1] - counter] == ""):
                        return True
                    counter += 1

                if from_location[1] - counter != to_location[1] and game_board[from_location[0]][from_location[1] - counter] != "":
                    counter += 1
                    while game_board[from_location[0]][from_location[1] - counter] == "":
                        counter += 1

                    if game_board[from_location[0]][from_location[1] - counter].get_team() == "black":
                        if from_location[1] - counter == to_location[1]:
                            return True

            if from_location[1] == to_location[1] and to_location[0] > from_location[0]:  # if moving to the up same column
                counter = 1
                while game_board[from_location[0] + counter][from_location[1]] == "":
                    if from_location[0] + counter == to_location[0] and (game_board[from_location[0] + counter][from_location[1]] == ""):
                        return True
                    counter += 1

                if from_location[0] + counter != to_location[0] and game_board[from_location[0] + counter][from_location[1]] != "":
                    counter += 1
                    while game_board[from_location[0] + counter][from_location[1]] == "":
                        counter += 1

                    if game_board[from_location[0] + counter][from_location[1]].get_team() == "black":
                        if from_location[0] + counter == to_location[0]:
                            return True

            if from_location[1] == to_location[1] and to_location[0] < from_location[0]:  # if moving down the same column
                counter = 1
                while game_board[from_location[0] - counter][from_location[1]] == "":
                    if from_location[0] - counter == to_location[0] and (game_board[from_location[0] - counter][from_location[1]] == ""):
                        return True
                    counter += 1

                if from_location[0] - counter != to_location[0] and game_board[from_location[0] - counter][from_location[1]] != "":
                    counter += 1
                    while game_board[from_location[0] - counter][from_location[1]] == "":
                        counter += 1

                    if game_board[from_location[0] - counter][from_location[1]].get_team() == "black":
                        if from_location[0] - counter == to_location[0]:
                            return True

        if self.get_team() == "black":
            if from_location[0] == to_location[0] and to_location[1] > from_location[1]:  # if moving to the right same row
                counter = 1
                while game_board[from_location[0]][from_location[1] + counter] == "":
                    if from_location[1] + counter == to_location[1] and (
                            game_board[from_location[0]][from_location[1] + counter] == ""):
                        return True
                    counter += 1

                if from_location[1] + counter != to_location[1] and game_board[from_location[0]][from_location[1] + counter] != "":
                    counter += 1
                    while game_board[from_location[0]][from_location[1] + counter] == "" and from_location[1] + counter < 8:
                        counter += 1

                    if game_board[from_location[0]][from_location[1] + counter] == "":
                        return False

                    if game_board[from_location[0]][from_location[1] + counter].get_team() == "red":
                        if from_location[1] + counter == to_location[1]:
                            return True

            elif from_location[0] == to_location[0] and to_location[1] < from_location[1]:  # if moving to the left same row
                counter = 1
                while game_board[from_location[0]][from_location[1] - counter] == "":
                    if from_location[1] - counter == to_location[1] and (
                            game_board[from_location[0]][from_location[1] - counter] == ""):
                        return True
                    counter += 1

                if from_location[1] - counter != to_location[1] and game_board[from_location[0]][from_location[1] - counter] != "":
                    counter += 1
                    while game_board[from_location[0]][from_location[1] - counter] == "":
                        counter += 1

                    if game_board[from_location[0]][from_location[1] - counter].get_team() == "red":
                        if from_location[1] - counter == to_location[1]:
                            return True

            elif from_location[1] == to_location[1] and to_location[0] > from_location[0]:  # if moving to the up same column
                counter = 1
                while game_board[from_location[0] + counter][from_location[1]] == "":
                    if from_location[0] + counter == to_location[0] and (game_board[from_location[0] + counter][from_location[1]] == ""):
                        return True
                    counter += 1

                if from_location[0] + counter != to_location[0] and game_board[from_location[0] + counter][from_location[1]] != "":
                    counter += 1
                    while game_board[from_location[0] + counter][from_location[1]] == "":
                        counter += 1

                    if game_board[from_location[0] + counter][from_location[1]].get_team() == "red":
                        if from_location[0] + counter == to_location[0]:
                            return True

            elif from_location[1] == to_location[1] and to_location[0] < from_location[0]:  # if moving down the same column
                counter = 1
                while game_board[from_location[0] - counter][from_location[1]] == "":
                    if from_location[0] - counter == to_location[0] and (
                            game_board[from_location[0] - counter][from_location[1]] == ""):
                        return True
                    counter += 1

                if from_location[0] - counter != to_location[0] and game_board[from_location[0] - counter][from_location[1]] != "":
                    counter += 1
                    while game_board[from_location[0] - counter][from_location[1]] == "":
                        counter += 1
                    if game_board[from_location[0] - counter][from_location[1]].get_team() == "red":
                        if from_location[0] - counter == to_location[0]:
                            return True

        return False

class Soldier(PlayerPiece):
    """Represents a soldier piece on the game board. The class inherits from the PLayerPiece class with its own
    unique get_legal_move function"""

    def get_legal_move(self, game_board, from_location, to_location):
        """Takes as a parameter a board and returns a list of legal moves for the soldier piece"""

        if self.get_team() == "black" and from_location[0] < to_location[0]:  # return False if black moving backwards
            return False

        if self.get_team() == "red" and from_location[0] > to_location[0]: # return False if red moving backwards
            return False

        # check if black is on its side of the river and trying to move horizontally when not allowed
        if self.get_team() == "black" and from_location[0] >= 5 and (from_location[1] < to_location[1] or from_location[1] > to_location[1]):
            return False

        # check if red is on its side of the river and trying to move horizontally when not allowed
        if self.get_team() == "red" and from_location[0] <= 4 and (from_location[1] < to_location[1] or from_location[1] > to_location[1]):
            return False

        if self.get_team() == "red" and from_location[0] <= 4 and (from_location[0] + 1 == to_location[0] and from_location[1] == to_location[1]):
            if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                return True

        elif self.get_team() == "red" and from_location[0] >= 5:
            if from_location[0] + 1 == to_location[0] and from_location[1] == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] == to_location[0] and from_location[1] + 1 == to_location[1]:  # moving to the right
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "black":
                    return True

            elif from_location[0] == to_location[0] and from_location[1] - 1 == to_location[1]:  # moving to the left
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][
                    to_location[1]].get_team() == "black":
                    return True

        if self.get_team() == "black" and from_location[0] >= 5 and (from_location[0] - 1 == to_location[0] and from_location[1] == to_location[1]):
            if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                return True

        elif self.get_team() == "black" and from_location[0] <= 4:
            if from_location[0] - 1 == to_location[0] and from_location[1] == to_location[1]:
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] == to_location[0] and from_location[1] + 1 == to_location[1]:  # moving to the right
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

            elif from_location[0] == to_location[0] and from_location[1] - 1 == to_location[1]:  # moving to the left
                if game_board[to_location[0]][to_location[1]] == "" or game_board[to_location[0]][to_location[1]].get_team() == "red":
                    return True

        return False

