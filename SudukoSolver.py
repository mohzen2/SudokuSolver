from pprint import pprint


def find_empty(puzzle):
    # finds next row or coloumn to move to. represent spaces with -1
    # returns the row, coloumn tuple ( or (None, None) if there is none)

    # keep in mind that we are using 0 - 8 for our indicies
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def valid(puzzle, guess, row, col):
    # finds out wether each guess is correct or not
    # return true if valid and false if not
    # rules of sudoko no row, coloumn, or 3x3 matrix can have repeating values
    row_values = puzzle[row]
    if guess in row_values:
        return False

    # now we'll check column
    # col_values = []
    # for i in range(9):
    #    col_values.append(puzzle[i][col])
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False

    # now we have to check squares
    # 3x3 matricies
    row_start = (row // 3) * 3
    col_start = (col //3) *3

    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True # meaning all the checks were passed


def SudokoSolver(puzzle):
    # we will solve Sudoko using a back tracking technique
    # our puzzle consists a list of lists, inner lists a row in puzzle 
    # If solution exsits we place the number



    # step 1) analyze given numbers and select a starting point
    row, col = find_empty(puzzle)

    # step 1a if nothing left, then should have completed puzzle succesfully
    if row is None:
        return True

    # step 2 if theres a place to put a number, make a guess between 1 and 9
    for guess in range(1, 10): # last number not in range
        # check if its a valid guess
        if valid(puzzle, guess, row, col):
            # now we should make a guess on what number goes where
            puzzle[row][col] = guess
            # now we should recurse through puzzle
            # continously call function until its sucessfully solved
            if SudokoSolver(puzzle):
                return True

        # if answer is not correct or does not succesfully solve puzzle
        # should go back and try a new integer
        puzzle[row][col] = -1

    # if we've recursed over all numbers and cant succesfull solve, say its unsolvable
    return False

if __name__ == '__main__': # remember this is good practice to isolate your code 
    # only run what you've written
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(SudokoSolver(example_board))
    print(example_board)



