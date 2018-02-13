# Problem Set 8
# Name: Kim, Matthew
# Collaborators: last name1, first name1; last name2, first name2; etc.

# Description: A solver for the Sudoku puzzle
import sys

def grid_display(board):
    """Display the board as a nice grid on the screen."""
    for j in range(9):
        for k in range(9):
            print board[j][k],
            if k%3 == 2:
                print '\t',
        print
        if j%3 == 2:
            print
    return None

def set_board(list_of_lines):
    """Set the board based on the list of lines read from the input file."""
    board = () # Empty tuple
    for line in list_of_lines:
        current_row = ()
        number_list = line.rstrip().split()
        for num in number_list:
            current_row += (int(num), )
        board += (current_row, )
    return board

def load_file(filename):
    try:
        # Open the selected file in read mode.
        file_object = open(filename, 'r')
    except IOError as err_msg:
        print "Couldn't open the file!", err_msg
        sys.exit()
    else:
        # Use the lines in the file to create the board.
        lines = file_object.readlines()
        board = set_board(lines)
        return board
    finally:
        file_object.close()

##############################################################################
# Complete the following functions
##############################################################################
def is_safe(board, row, column, x):
    if column_check(board,column) and row_check(board,row) and cluster_check(board,row,column):
        return True
    else:
        #print 'is_safe True'
        return False


def column_check(board, column):
    """Check the board at the given column index to verify if
    that column has a valid set of numbers.
    """
    lol = []
    new_board = board[:]
    for i in new_board:
        for j in i:
            if list(i).index(j) == column-1:
                lol.append(j)
    for x in range(1,10):
        if lol.count(x) >1:
            return False
    return True

def row_check(board, row):
    """Check the board at the given row index to verify if that
    row has a valid set of numbers.
    """
    lol = []
    for i in range(9):
        if row-1 == i:
            for j in board[row-1]:
                lol.append(j)
    for x in range(1,10):
        if  lol.count(x) > 1:
            return False
    else:
        return True



def cluster_check(board, row, column):
    """Check the cluster at the given column and row indices to
    verify if that cluster has a valid set of numbers.
    """
    lol = []
    if row >= 1 and row <=3:
        row_stick = (board[0:3])
    elif row >= 4 and row <= 6:
        row_stick = (board[3:6])
    elif row>=7 and row<=9:
        row_stick = (board[6:])
    if column>= 1 and column <=3:
        row_block = (row_stick[0][0:3])+(row_stick[1][0:3])+(row_stick[2][0:3])
    elif column >=4 and column <=6:
        row_block = (row_stick[0][3:6])+(row_stick[1][3:6])+(row_stick[2][3:6])
    elif column >=7 and column <=9:
        row_block = (row_stick[0][6:])+(row_stick[1][6:])+(row_stick[2][6:])
    for i in row_block:
        lol.append(i)
    for x in range(1,10):
        if  lol.count(x) > 1:
            return False
    else:
        return True
def place(board,row,column,x):
    """Update the given puzzle board.
    Place digit x at the given row and column, and return
    the new board.
    """
    new_board = list(board)
    new_board[row-1] = new_board[row-1][:column-1] + (x, ) + new_board[row-1][column:]
    newer_board = tuple(new_board)
    return newer_board
    
def first_empty(board):

    """Return a tuple (row, col) which represents the row and
    column of an empty cell (one that has the value zero). If no
    such cell exists (which means the puzzle is solved), return
    None.
    """
    for x in list(board):
        for i in list(x):
            if i == 0:
                return (list(board).index(x)+1,list(x).index(i)+1)
    return None 
            



def sudoku_solve(board):
    """Call this function to solve the Sudoku board.
    It should call the recursive function solve_helper.
    """
    if first_empty(board) == None:
        return board
    solution = solve_helper(board, 1, 1)
    return solution


def solve_helper(board, row, col):
    if first_empty(board) == None:
        return board
    for x in range (1, len(board)+1):
        if is_safe(board, row, col, x):
            new_board = place(board,row,col,x)
            empty_cell = first_empty(new_board)
            if first_empty(new_board) == None:
                solution = new_board
                return solution
            solution = solve_helper(new_board,empty_cell[0],empty_cell[1])
            if solution != None:    
                return solution
    return None


######__main__
#### Test 1: Please do not change the following four lines. If you're getting
# an error here, it means one of the following functions is not working
# properly: row_check, column_check, cluster_check
new_board = place(load_file('easy.txt'), 1, 1, 1)
assert row_check(new_board, 1), 'Row check failed!'
assert column_check(new_board, 1), 'Column check failed!'
assert cluster_check(new_board, 1, 1), 'Cluster check failed!'

#### Test 2: Please do not change the following four lines. If you're getting
# an error here, it means one of the following functions is not working
# properly: row_check, column_check, cluster_check
new_board = place(load_file('easy.txt'), 3, 7, 3)
assert not row_check(new_board, 3), 'Row check failed!'
assert column_check(new_board, 7), 'Column check failed!'
assert not cluster_check(new_board, 3, 7), 'Cluster check failed!'


### Update the file name below accordingly.
### Choices: 'easy.txt'     'moderate.txt'      'hard.txt'
board = load_file('easy.txt')
# The function call to solve the Sudoku puzzle.
solution = sudoku_solve(board)
# The function call to display the solution board.
grid_display(solution)


