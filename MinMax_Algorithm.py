# Importing necessary libraries
import pygame
from copy import deepcopy

# Global variable
depth = 0

# Color constants
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def MiniMAx(pos, depth, max_pl, game):
    """
    This function implements the MiniMax algorithm to find the best move for a given position.

    Returns:
    tuple: A tuple containing the evaluation of the position and the best move for the current position.
    """

    # If the depth is 0 or the position is a terminal position, return the evaluation of the position
    if depth == 0 or pos.winner() != None:
        return pos.eval(), pos

    # If the current player is the maximizer
    if max_pl:
        # Initialize the max evaluation to negative infinity
        maxEval = float('-inf')
        # Initialize the best move to None
        best_M = None
        # Iterate through all the possible moves
        for move in get_all_m(pos, WHITE, game):
            # Get the evaluation of the move
            evaluation = MiniMAx(move, depth - 1, False, game)[0]
            # Update the max evaluation
            maxEval = max(maxEval, evaluation)
            # If the evaluation is equal to the max evaluation, update the best move
            if maxEval == evaluation:
                best_M = move
        # Return the max evaluation and the best move
        return maxEval, best_M

    # If the current player is the minimizer
    else:
        # Initialize the min evaluation to positive infinity
        minEval = float('inf')
        # Initialize the best move to None
        best_M = None
        # Iterate through all the possible moves
        for move in get_all_m(pos, RED, game):
            # Get the evaluation of the move
            evaluation = MiniMAx(move, depth - 1, True, game)[0]
            # Update the min evaluation
            minEval = min(minEval, evaluation)
            # If the evaluation is equal to the min evaluation, update the best move
            if minEval == evaluation:
                best_M = move
        # Return the min evaluation and the best move
        return minEval, best_M


def get_all_m(board, color, game):
    """
    This function returns all the possible moves for a given board and color.
    Returns:
    list: A list of all the possible moves.
    """

    # Initialize the list of moves
    moves = []
    # Iterate through all the pieces of the given color
    for piece in board.get_all_pieces(color):
        # Get the valid moves for the piece
        valid_moves = board.get_valid_moves(piece)
        # Iterate through all the valid moves
        for move, skip in valid_moves.items():
            # Draw the moves
            draw_moves(game, board, piece)
            # Make a deep copy of the board
            temp_board = deepcopy(board)
            # Get the piece from the board
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            # Simulate the move
            new_board = simul_move(temp_piece, move, temp_board, game, skip)
            # Append the board to the list of moves
            moves.append(new_board)
    # Return the list of moves
    return moves


def simul_move(piece, move, board, game, skip):
    """
    This function simulates the move on the board.

    Returns:
    object: The board object after the move is made.
    """

    # Make the move on the board
    board.move(piece, move[0], move[1])
    # If the move is a skip move, remove the piece
    if skip:
        board.remove(skip)
    # Return the board
    return board


def draw_moves(game, board, piece):
    """
    This function draws the moves on the board.

    """

    # Get the valid moves for the piece
    valid_moves = board.get_valid_moves(piece)
    # Draw the board
    board.draw(game.win)
    # Draw the circle around the piece
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    # Draw the valid moves
    game.draw_moves(valid_moves.keys())
    # Update the display
    pygame.display.update()
    # Delay for 10 milliseconds
    pygame.time.delay(10)
