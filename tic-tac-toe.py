import tkinter as tk
from tkinter import messagebox
from math import inf
from tkinter import Toplevel
import sys

# Game board size
n = int(input("Enter a number between 3 and 10 (n): "))

# Check the validity of the input
if  not 3 <= n <= 10:
    print("Invalid input.Try again!!")
    sys.exit()
    


# Global variable to store the difficulty level
difficulty = "Hard"  # Default difficulty level

def custom_messagebox(title, message):
    # Create a new window
    message_window = tk.Toplevel(root)
    message_window.title(title)
    message_window.config(bg='black')  # Set background color to black
    message_window.geometry("300x150")  # Set window size

    # Add text
    message_label = tk.Label(message_window, text=message, fg='green', bg='black', font=('Helvetica', 12))
    message_label.pack(pady=20)

    # Add a button to close the window
    button_close = tk.Button(message_window, text="OK!", command=message_window.destroy, width=10, height=2,
                             font=('Helvetica', 12))
    button_close.pack(pady=5)

class Custom_dialog:
    # Custom dialog box for user input.
    def __init__(self, parent, title, prompt, minvalue, maxvalue):
        self.top = Toplevel(parent)
        self.top.title(title)
        self.top.config(bg='black')
        self.top.geometry("300x150")  # Set window size

        self.label = tk.Label(self.top, text=prompt, fg='green', bg='black', font=('Helvetica', 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.top, fg='green', bg='black', font=('Helvetica', 12))
        self.entry.pack(pady=5)

        self.button = tk.Button(self.top, text="Submit", command=self.on_submit, fg='green', bg='black',
                                font=('Helvetica', 12))
        self.button.pack(pady=5)

        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.result = None

    def on_submit(self):
        # Callback function for the submit button.
        try:
            value = int(self.entry.get())
            if self.minvalue <= value <= self.maxvalue:
                self.result = value
                self.top.destroy()
            else:
                custom_messagebox("Error", f"Value must be between {self.minvalue} and {self.maxvalue}")
        except ValueError:
            custom_messagebox("Error", "Please enter a valid integer")

    def show(self):
        # Display the dialog and wait for user input.
        # Returns the result after the dialog is closed.
        self.top.grab_set()
        self.top.wait_window()
        return self.result


def selectDifficulty(level):
    global difficulty
    difficulty = level
    custom_messagebox("Difficulty Set", f"Difficulty set to {difficulty}")

def Clearboard(board):
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            board[x][y] = 0

def winningPlayer(board, player):
    for i in range(n):
        if all([board[i][j] == player for j in range(n)]) or all([board[j][i] == player for j in range(n)]):
            return True

    if all([board[i][i] == player for i in range(n)]) or all([board[i][n-1-i] == player for i in range(n)]):
        return True

    return False

def gameWon(board):
    return winningPlayer(board, 1) or winningPlayer(board, -1)

def blanks(board):
    blank = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if board[x][y] == 0:
                blank.append([x, y])
    return blank

def boardFull(board):
    return len(blanks(board)) == 0

def setMove(board, x, y, player):
    board[x][y] = player

def getScore(board):
    if winningPlayer(board, 1):
        return 10
    elif winningPlayer(board, -1):
        return -10
    else:
        return 0

def abminimax(board, depth, alpha, beta, player):


    row = -1
    col = -1
    if depth == 0 or gameWon(board):
        return [row, col, getScore(board)]

    for cell in blanks(board):
        setMove(board, cell[0], cell[1], player)
        score = abminimax(board, depth - 1, alpha, beta, -player)
        setMove(board, cell[0], cell[1], 0)

        if player == 1:
            if score[2] > alpha:
                alpha = score[2]
                row = cell[0]
                col = cell[1]
            print(f"Maximizer: Depth={depth}, Alpha={alpha}, Beta={beta}, Move=({row}, {col})")
        else:
            if score[2] < beta:
                beta = score[2]
                row = cell[0]
                col = cell[1]
            print(f"Minimizer: Depth={depth}, Alpha={alpha}, Beta={beta}, Move=({row}, {col})")

        if alpha >= beta:
            print("Alpha-Beta Pruning!!!")
            break

    return [row, col, alpha if player == 1 else beta]

def findWinningMove(board, player):
    for cell in blanks(board):
        setMove(board, cell[0], cell[1], player)
        if winningPlayer(board, player):
            setMove(board, cell[0], cell[1], 0)
            return (cell[0], cell[1])
        setMove(board, cell[0], cell[1], 0)
    return None

def o_comp(board):
    move = findWinningMove(board, -1)
    if move:
        setMove(board, move[0], move[1], -1)
    else:
        if n==3:
            depth = len(blanks(board))
        if n!=3:
            depth = min(len(blanks(board)), 4)  # Maximum depth is 4
        if difficulty == "Easy":
            depth = min(depth, 1)  # In Easy mode, maximum depth is 1
        result = abminimax(board, depth, -inf, inf, -1)
        setMove(board, result[0], result[1], -1)

    Gameboard_GUI()
    checkBoardState()

def Gameboard_GUI():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                buttons[i][j].config(text='X', fg='green', bg='black', state='normal')
            elif board[i][j] == -1:
                buttons[i][j].config(text='O', fg='green', bg='black', state='normal')
            else:
                buttons[i][j].config(text=' ', fg='green', bg='black', state='normal')



def playerMove_GUI(x, y):
    if board[x][y] == 0:
        setMove(board, x, y, 1)
        Gameboard_GUI()
        if not gameWon(board) and not boardFull(board):
            o_comp(board)
        else:
            checkBoardState()


def show_message_and_clear_board(message):
    messagebox.showinfo("Message", message)
    Clearboard(board)

def checkBoardState():
    if gameWon(board):
        result = 'X has won!' if winningPlayer(board, 1) else 'O has won!'
        show_message_and_clear_board(result)
    elif boardFull(board):
        show_message_and_clear_board("It's a draw")
    Gameboard_GUI()

def changeBoardSize():
    global n, board, root
    dialog = Custom_dialog(root, "Board Size", "Enter the new board size (n):", 3, 10)
    newSize = dialog.show()
    if newSize and newSize != n:
        n = newSize
        board = [[0 for _ in range(n)] for _ in range(n)]
        restartGUI()


def restartGUI():
    global root
    if root:
        root.destroy()  # Close the old window
    setupGUI()

def selectDifficulty(level):
    global difficulty
    difficulty = level
    custom_messagebox("Difficulty Set", f"Difficulty set to {difficulty}")

# GUI Setup
def setupGUI():
    global root, buttons
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Buttons for selecting difficulty and changing board size
    easy_button = tk.Button(root, text="Easy", command=lambda: selectDifficulty("Easy"))
    hard_button = tk.Button(root, text="Hard", command=lambda: selectDifficulty("Hard"))
    size_button = tk.Button(root, text="Change Size", command=changeBoardSize)
    easy_button.grid(row=n, column=0)
    hard_button.grid(row=n, column=1)
    size_button.grid(row=n, column=2)

    # Game board buttons
    buttons = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            buttons[i][j] = tk.Button(root, text=' ', font=('normal', 40), height=1, width=2,
                                      command=lambda i=i, j=j: playerMove_GUI(i, j))
            buttons[i][j].grid(row=i, column=j)

    Gameboard_GUI()
    root.mainloop()

board = [[0 for _ in range(n)] for _ in range(n)]
setupGUI()
