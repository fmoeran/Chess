
column_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
piece_letters = ["P", "N", "B", "R", "Q", "K", "p", "n", "b", "r", "q", "k"]

piece_values = {piece: val for val, piece in enumerate(piece_letters)}
white_pieces = [piece_values[letter] for letter in piece_letters[:len(piece_letters) // 2]]
black_pieces = [piece_values[letter] for letter in piece_letters[len(piece_letters) // 2:]]

piece_colours = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]  # 0 == white, 1 == black

king_moves = [-9, -8, -7, -1, 1, 7, 8, 9]


piece_worths = {
    "p": 100,
    "n": 300,
    "b": 350,
    "r": 500,
    "q": 900,
}


piece_square = {
    "P": [0, 0, 0, 0, 0, 0, 0, 0,
          50, 50, 50, 50, 50, 50, 50, 50,
          10, 10, 20, 30, 30, 20, 10, 10,
          5, 5, 10, 25, 25, 10, 5, 5,
          0, 0, 0, 20, 20, 0, 0, 0,
          5, -5, -10, 0, 0, -10, -5, 5,
          5, 10, 10, -20, -20, 10, 10, 5,
          0, 0, 0, 0, 0, 0, 0, 0],
    "N": [-50, -40, -30, -30, -30, -30, -40, -50,
          -40, -20, 0, 5, 5, 0, -20, -40,
          -30, 5, 10, 15, 15, 10, 5, -30,
          -30, 0, 15, 20, 20, 15, 0, -30,
          -30, 5, 15, 20, 20, 15, 5, -30,
          -30, 0, 10, 15, 15, 10, 0, -30,
          -40, -20, 0, 0, 0, 0, -20, -40,
          -50, -40, -30, -30, -30, -30, -40, -50],
    "B": [-20, -10, -10, -10, -10, -10, -10, -20,
          -10, 0, 0, 0, 0, 0, 0, -10,
          -10, 0, 5, 10, 10, 5, 0, -10,
          -10, 5, 5, 10, 10, 5, 5, -10,
          -10, 0, 10, 10, 10, 10, 0, -10,
          -10, 10, 10, 10, 10, 10, 10, -10,
          -10, 5, 0, 0, 0, 0, 5, -10,
          -20, -10, -10, -10, -10, -10, -10, -20],
    "R": [0, 0, 0, 0, 0, 0, 0, 0,
          5, 10, 10, 10, 10, 10, 10, 5,
          -5, 0, 0, 0, 0, 0, 0, -5,
          -5, 0, 0, 0, 0, 0, 0, -5,
          -5, 0, 0, 0, 0, 0, 0, -5,
          -5, 0, 0, 0, 0, 0, 0, -5,
          -5, 0, 0, 0, 0, 0, 0, -5,
           0, 0, 0, 5, 5, 0, 0, 0],
    "Q": [-20, -10, -10, -5, -5, -10, -10, -20,
          -10, 0, 0, 0, 0, 5, 0, -10,
          -10, 0, 5, 5, 5, 5, 5, -10,
          -5, 0, 5, 5, 5, 5, 0, 0,
          -5, 0, 5, 5, 5, 5, 0, -5,
          -10, 0, 5, 5, 5, 5, 0, -10,
          -10, 0, 0, 0, 0, 0, 0, -10,
          -20, -10, -10, -5,-5, -10, -10, -20],
    "K": [-30, -40, -40, -50, -50, -40, -40, -30,
          -30, -40, -40, -50, -50, -40, -40, -30,
          -30, -40, -40, -50, -50, -40, -40, -30,
          -30, -40, -40, -50, -50, -40, -40, -30,
          -20, -30, -30, -40, -40, -30, -30, 20,
          -10, -20, -20, -20, -20, -20, -20, -10,
          20, 20, 0, 0, 0, 0, 20, 20,
          20, 30, 10, 0, 0, 10, 30, 20],

}
# make the black versions
black_piece_squares = [(piece.lower(), table[::-1]) for piece, table in piece_square.items()]
for piece, table in black_piece_squares:
    piece_square[piece] = table

#print(piece_square.items())

