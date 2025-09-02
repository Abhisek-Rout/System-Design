# Create a prtotype interface
from abc import ABC, abstractmethod

class Prototype:
    @abstractmethod
    def clone(self):
        pass

from typing import List

class GamePiece(Prototype):
    def __init__(self, color: str, position: int):
        self.__color = color
        self.__position = position

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        self.__position = value

    def __str__(self):
        return f"GamePiece(color={self.color}, position={self.position})"
    
    def clone(self):
        return GamePiece(self.color, self.position)

class GameBoard(Prototype):
    def __init__(self):
        self.pieces: List[GamePiece] = list()

    def add_piece(self, piece: GamePiece):
        self.pieces.append(piece)

    def get_pieces(self):
        return self.pieces
    
    def show_board_state(self):
        print("Current board state")
        for piece in self.pieces:
            print(piece)

    def clone(self):
        new_game_board: GameBoard = GameBoard()
        for piece in self.get_pieces():
            new_game_board.add_piece(piece.clone())
        return new_game_board


class WithPrototypePattern:
    def main(self):
        game_board: GameBoard = GameBoard()
        game_board.add_piece(GamePiece("Red", 1))
        game_board.add_piece(GamePiece("Blue", 5))
        print("Original Board")
        game_board.show_board_state()

        # Checkpoint this state
        copied_board: GameBoard = game_board.clone()
        print("Copied board")
        copied_board.show_board_state()
        


if __name__ == "__main__":
    obj: WithPrototypePattern = WithPrototypePattern()
    obj.main()