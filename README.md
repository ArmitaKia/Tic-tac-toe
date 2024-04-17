# Tic-Tac-Toe Game in Python

This is a simple implementation of the classic Tic-Tac-Toe (X and O) game using Python and the tkinter library for the graphical user interface. The game allows you to play against the computer, which uses the Minimax algorithm with Alpha-Beta Pruning for AI strategy. You can also choose the difficulty level (Easy or Hard) and change the board size (3x3 to 10x10) as per your preference.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system.

### Installation

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where you've placed the code.

## Algorithm Overview

The AI strategy used in this Tic-Tac-Toe game is based on the Minimax algorithm with Alpha-Beta Pruning. Here's a brief overview of how it works:

- Minimax is a decision-making algorithm commonly used in two-player games, like Tic-Tac-Toe. It explores all possible game states by recursively simulating moves and predicting the outcome.

- In each recursive step, the algorithm evaluates the current state of the game and assigns a score to it. The goal is to find the best move that maximizes the AI's chances of winning and minimizes the opponent's chances.

- Alpha-Beta Pruning is an optimization technique that reduces the number of nodes the algorithm needs to evaluate. It maintains two values, alpha and beta, which represent the minimum score the maximizing player is assured of and the maximum score the minimizing player is assured of, respectively.

- During the search, if the algorithm finds a move that leads to a state worse than what the opponent has already achieved (i.e., a score less than beta in a maximizing node or a score greater than alpha in a minimizing node), it can prune that branch of the search tree and avoid further exploration.

## Code Overview

- The code provides a graphical user interface for the Tic-Tac-Toe game, allowing you to play against the computer, which employs the Minimax algorithm with Alpha-Beta Pruning for decision making.

- You can choose the difficulty level (Easy or Hard) for the computer opponent, and you can also change the board size from 3x3 to 10x10.

- The AI player (O) uses the Minimax algorithm to determine its moves, making it challenging to beat in the Hard mode.

- The game checks for a win condition, a draw, or ongoing play after each move and provides feedback to the user.

- You can customize the code further or contribute to its development based on your requirements.

### Evaluator function

If the first player wins, which is the user, the value is 10, and if the algorithm wins, it returns a negative value of 10, which is a sign of the user's loss, and if neither happens, it returns 0.

## Acknowledgments

This project is inspired by the classic Tic-Tac-Toe game and the Minimax algorithm. It's an educational and fun way to explore AI strategy in a simple game.


