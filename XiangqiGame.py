# Author: Anthony Corton
# Date: 02/11/2020
# Description: Contains a class named XiangqiGame for an abstract game known as Xiangqi. The class contains
#              methods for getting game state, checking for if a player is in check, making moves on the board,
#              and a couple other methods


class XiangqiGame:
    """Represents an abstract game known as xiangqi with methods for getting game state, checking if a player is
    in check, and method for making moves."""

    def __init__(self):
        """Returns an xiangqi board game object with game state initalized to UNFINISHED and the board setup"""
        self._game_state = "UNFINISHED"
        self._board = []
        self._turn_counter = 1                  # keeps track of the turns, if odd it is red if even it is black

        black_king = King("black", "b_king", [9, 4])
        black_guard_l = Guard("black", "b_guard", [9, 3])
        black_elephant_l = Elephant("black", "b_ele", [9, 2])
        black_horse_l = Horse("black", "b_horse", [9, 1])
        black_chariot_l = Chariot("black", "b_char", [9, 0])
        black_cannon_l = Cannon("black", "b_can", [7, 1])
        black_soldier_l_1 = Soldier("black", "b_sol", [6, 0])

        black_guard_r = Guard("black", "b_guard", [9, 5])
        black_elephant_r = Elephant("black", "b_ele", [9, 6])
        black_horse_r = Horse("black", "b_horse", [9, 7])
        black_chariot_r = Chariot("black", "b_char", [9, 8])
        black_cannon_r = Cannon("black", "b_can", [7, 7])
        black_soldier_r_1 = Soldier("black", "b_sol", [6, 8])

        black_soldier_l_2 = Soldier("black", "b_sol", [6, 2])
        black_soldier_m = Soldier("black", "b_sol", [6, 4])
        black_soldier_r_2 = Soldier("black", "b_sol", [6, 6])

        red_king = King("red", "r_king", [0, 4])
        red_guard_l = Guard("red", "r_guard", [0,3])
        red_elephant_l = Elephant("red", "r_ele", [0, 2])
        red_horse_l = Horse("red", "r_horse", [0, 1])
        red_chariot_l = Chariot("red", "r_char", [0,0])
        red_cannon_l = Cannon("red", "r_can", [2, 1])
        red_soldier_l_1 = Soldier("red", "r_sol", [3,0])

        red_guard_r = Guard("red", "r_guard", [0, 5])
        red_elephant_r = Elephant("red", "r_ele", [0, 6])
        red_horse_r = Horse("red", "r_horse", [0, 7])
        red_chariot_r = Chariot("red", "r_char", [0, 8])
        red_cannon_r = Cannon("red", "r_can", [2, 7])
        red_soldier_r_1 = Soldier("red", "r_sol", [3, 8])

        red_soldier_r_2 = Soldier("red", "r_sol", [3, 6])
        red_soldier_m = Soldier("red", "r_sol", [3, 4])
        red_soldier_l_2 = Soldier("red", "r_sol", [3, 2])

        for i in range(0, 10):
            if i == 0:
                self._board.append([red_chariot_l, red_horse_l, red_elephant_l, red_guard_l, red_king, red_guard_r,
                                    red_elephant_r, red_horse_r, red_chariot_r])
            elif i == 2:
                self._board.append(["", red_cannon_l, "", "", "", "", "", red_cannon_r, ""])
            elif i == 3:
                self._board.append([red_soldier_l_1, "", red_soldier_l_2, "", red_soldier_m, "", red_soldier_r_2, "", red_soldier_r_1])
            elif i == 6:
                self._board.append([black_soldier_l_1, "", black_soldier_l_2, "", black_soldier_m, "", black_soldier_r_2, "",
                                    black_soldier_r_1])
            elif i == 7:
                self._board.append(["", black_cannon_l, "", "", "", "", "", black_cannon_r, ""])
            elif i == 9:
                self._board.append([black_chariot_l, black_horse_l, black_elephant_l,
                                    black_guard_l, black_king, black_guard_r, black_elephant_r, black_horse_r, black_chariot_r])
            else:
                self._board.append(["", "", "", "", "", "", "", "", ""])
            # lowercase is black uppercase is red, ca = cannon, p = pawn, c = chariot, h = horse, e = elephant
            # g = guard, k = king
            self._board_key = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8}
            #the board key contains the corresponding columns for letters

    def get_game_state(self):
        """Returns the state of the game"""
        return self._game_state

    def get_all_legal_moves(self, piece_object):
        """Takes as a parameter a piece object and returns a list of all the legal moves for that object"""
        list_legal_moves = []

        for row in range(10):
            for column in range(9):
                to_local = []
                test_move = piece_object.get_legal_move(self._board, piece_object.get_location(), [row, column])
                if test_move is True:
                    move = []
                    move.append(row)
                    move.append(column)
                    list_legal_moves.append(move)

        return list_legal_moves

    def display_game_state(self):
        """Prints the game board for debugging purposes"""
        row_list = list(self._board)        # copy board
        row_counter = 0                     # row and column counter keep tracks for indexing
        column_counter = 0
        print([" A "], [" B "], [" C "], [" D "], [" E "], [" F "], [" G "], [" H "], [" I "])
        while row_counter < 10:
            print([row_counter + 1], end=' ')
            while column_counter < 9:
                if issubclass(row_list[row_counter][column_counter].__class__, PlayerPiece) is True:
                    print(row_list[row_counter][column_counter].get_piece(), end=' ')
                else:
                    print('"     "', end = ' ')
                column_counter += 1
            print("")
            row_counter += 1             # reset column counter so it starts from column 0 again
            column_counter = 0

    def flying_general(self):
        """Takes as a parameter a player icon and returns True if the general is in check because of flying general and
         False if otherwise"""

        black_king_coordinates = []
        red_king_coordinates = []

        # get coordinates of the red king
        for num in range(10):
            for num_column in range (9):
                if self._board[num][num_column] != "":
                    object = self._board[num][num_column]
                    if object.get_piece() == "r_king":          # get king location
                        red_king_coordinates.append(num)
                        red_king_coordinates.append(num_column)
                        break

        # get coordinates of the black king
        for num in range(10):
            for num_column in range(9):
                if self._board[num][num_column] != "":
                    object = self._board[num][num_column]
                    if object.get_piece() == "b_king":  # get king location
                        black_king_coordinates.append(num)
                        black_king_coordinates.append(num_column)
                        break

        if red_king_coordinates[1] != black_king_coordinates[1]:       # if Kings are not in same column return False
            return False

        else:
            counter = 1
            while self._board[red_king_coordinates[0] + counter][red_king_coordinates[1]] == "":
                counter += 1

            # if there is a piece in the same column as red king and it is not black king return false because not
            # flying general condition since there is a piece between the two kings
            if self._board[red_king_coordinates[0] + counter][red_king_coordinates[1]].get_piece() != "b_king":
                return False
            else:
                return True

        return False


    def check_for_win(self, player_icon):
        """Takes as a parameter a player icon and checks to see if that player has any legal move that allow them to get
        out of check.  If no moves can get them out of check then the opposing player wins.  This function is called
        by the make move only"""
        king_coordinates = []
        opposing_piece = []
        piece_counter = 0
        object = 0
        red_pieces = []
        red_coordinates = []

        if player_icon == "black":  # similar logic to locating king piece for black

            for num in range(10):
                for num_column in range(9):
                    if self._board[num][num_column] != "":
                        object = self._board[num][num_column]
                        if object.get_team() == "black":  # get king location
                            red_pieces.append(object)
            safe_copy = self._board.copy()

            for piece in red_pieces:
                list_of_moves = self.get_all_legal_moves(piece)

                for move in list_of_moves:
                    copy_board = self._board.copy()
                    from_location = piece.get_location()

                    potential_object = self._board[move[0]][move[1]]
                    self._board[from_location[0]][from_location[1]] = ""
                    self._board[move[0]][move[1]] = piece

                    if self.is_in_check("black") is True or self.flying_general():
                        self._board[from_location[0]][from_location[1]] = piece
                        self._board[move[0]][move[1]] = potential_object
                    else:
                        self._board[from_location[0]][from_location[1]] = piece
                        self._board[move[0]][move[1]] = potential_object
                        return
            self._board = safe_copy

            self._game_state = "RED_WON"

        if player_icon == "red":  # similar logic to locating king piece for black

            for num in range(10):
                for num_column in range(9):
                    if self._board[num][num_column] != "":
                        object = self._board[num][num_column]
                        if object.get_team() == "red":  # get king location
                            red_pieces.append(object)
            safe_copy = self._board.copy()

            for piece in red_pieces:
                list_of_moves = self.get_all_legal_moves(piece)

                for move in list_of_moves:
                    copy_board = self._board.copy()
                    from_location = piece.get_location()

                    potential_object = self._board[move[0]][move[1]]
                    self._board[from_location[0]][from_location[1]] = ""
                    self._board[move[0]][move[1]] = piece

                    if self.is_in_check("red") is True or self.flying_general():
                        self._board[from_location[0]][from_location[1]] = piece
                        self._board[move[0]][move[1]] = potential_object
                    else:
                        self._board[from_location[0]][from_location[1]] = piece
                        self._board[move[0]][move[1]] = potential_object
                        return
            self._board = safe_copy



            self._game_state = "BLACK_WON"



    def is_in_check(self, player_icon):
        """Takes as a parameter either red or black and return True if that player is in check or False if
         otherwise"""
        king_coordiantes = []

        if player_icon == "black":                  # check if player icon is black and if so get king locations
            for num in range(10):
                for num_column in range (9):
                    if self._board[num][num_column] != "":
                        object = self._board[num][num_column]
                        if object.get_piece() == "b_king":          # get king location
                            king_coordiantes.append(num)
                            king_coordiantes.append(num_column)
                            break


            for num in range(10):
                for num_column in range (9):
                    if self._board[num][num_column] != "":
                        object = self._board[num][num_column]
                        if object.get_team() == "red":              # locate and get location of opposing piece
                            potential_check_moves = object.get_legal_move(self._board, [num, num_column], king_coordiantes)
                            if potential_check_moves is True:
                                return True

        if player_icon == "red":                  # similar logic to locating king piece for black
            for num in range(10):
                for num_column in range (9):
                    if self._board[num][num_column] != "":
                        object = self._board[num][num_column]
                        if object.get_piece() == "r_king":          # get king location
                            king_coordiantes.append(num)
                            king_coordiantes.append(num_column)
                            break

        if player_icon == "red":
            for num in range(10):
                for num_column in range(9):
                    if self._board[num][num_column] != "":
                        object = self._board[num][num_column]
                        if object.get_team() == "black":  # locate and get location of opposing piece
                            potential_check_moves = object.get_legal_move(self._board, [num, num_column],
                                                                          king_coordiantes)
                            if potential_check_moves is True:
                                return True
        return False

    def make_move(self, string_from, string_to):
        """Takes two parameters first a string the piece is moving from and second the string the piece is moving to
        if the string from does not contain a piece, or the game has been won, or the move is illegal False is
        returned otherwise the function makes the move, removes any pieces if captured, updates, adn returns True"""

        if self.get_game_state() != "UNFINISHED":
            return False

        coordinate_list = [char for char in string_from]
        coordinate_list[1] = int(coordinate_list[1])
        column_value = self._board_key[coordinate_list[0]]
        piece_location = []

        if len(coordinate_list) > 2:        # necessary if user enters a row of 10
            coordinate_list[1] = str(coordinate_list[1]) + str(coordinate_list[2])
            coordinate_list[1] = int(coordinate_list[1])
            coordinate_list.remove(coordinate_list[2])

        if coordinate_list[0]  not in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:  # check to make sure in bounds
            return False

        if coordinate_list[1] > 10 or coordinate_list[1] < 1:  # return false if out of bounds of board
            return False

        row = coordinate_list[1] - 1
        piece_location.append(row)
        piece_location.append(column_value)

        if self._board[coordinate_list[1] - 1][column_value] == "":  # checks for if the from space has no piece
            return False

        piece_copy = self._board[coordinate_list[1] - 1][column_value]

        # check to make sure black only moves on even turns and red only on odd turns
        if piece_copy.get_team() == "black" and self._turn_counter % 2 != 0:
            return False

        if piece_copy.get_team() == "red" and self._turn_counter % 2 == 0:
            return False

        # if from space is not empty and has an piece object make list of to coordinates
        coordinate_list_to = [char for char in string_to]
        coordinate_list_to[1] = int(coordinate_list_to[1])

        if len(coordinate_list_to) > 2:
            coordinate_list_to[1] = str(coordinate_list_to[1]) + str(coordinate_list_to[2])
            coordinate_list_to[1] = int(coordinate_list_to[1])
            coordinate_list_to.remove(coordinate_list_to[2])

        if coordinate_list_to[0] not in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:  # check to make sure in bounds
            return False

        if coordinate_list_to[1] > 10 or coordinate_list_to[1] < 1:  # return false if out of bounds of board
            return False

        column_value_to = self._board_key[coordinate_list_to[0]]



        to_space = [(coordinate_list_to[1] - 1), column_value_to]

        piece_object = self._board[coordinate_list[1] - 1][column_value]
        legal_moves = piece_object.get_legal_move(self._board, piece_location, to_space)
        if legal_moves is True:                # if move the piece is moving to is legal to
            test_move = self._board.copy()
            self._board[to_space[0]][to_space[1]] = piece_object
            self._board[piece_location[0]][piece_location[1]] = ""

            if self.is_in_check(piece_object.get_team()) is True or self.flying_general() is True:     # check if move puts current player king in check

                self._board = test_move
                return False

            else:

                if piece_object.get_team() == "red":
                    if self.is_in_check("black"):
                        self.check_for_win("black")

                    else:
                        self.check_for_win("black")         # must check for stalemate even if not in check

                elif piece_object.get_team() == "black":
                    if self.is_in_check("red"):
                        self.check_for_win("red")

                    else:                           # if red not in check but has no legal moves
                        self.check_for_win("red")

            piece_object.set_location(to_space)
            self._turn_counter += 1
            return True

        return False


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

