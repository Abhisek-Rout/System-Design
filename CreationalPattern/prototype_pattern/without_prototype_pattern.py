from typing import List

class GamePiece:
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

class GameBoard:
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


class WithoutPrototypePattern:
    def main(self):
        game_board: GameBoard = GameBoard()
        game_board.add_piece(GamePiece("Red", 1))
        game_board.add_piece(GamePiece("Blue", 5))
        print("Original Board")
        game_board.show_board_state()

        # Checkpoint this state
        copied_board: GameBoard = GameBoard()
        for piece in game_board.get_pieces():
            copied_board.add_piece(piece.color, piece.position) # Deep copy if copied_board.add_piece(piece) it will be shallow copy

        print("Copied board")
        copied_board.show_board_state()
        


if __name__ == "__main__":
    obj: WithoutPrototypePattern = WithoutPrototypePattern()
    obj.main()

