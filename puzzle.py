import numpy

# --- BEGIN TEST CASES ---
goalState = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]

veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]

easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

doable = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]

oh_boy = [[8, 7, 1],
          [6, 0, 2],
          [5, 4, 3]]

impossible = [[0, 7, 2],
              [4, 6, 1],
              [3, 5, 8]]

# --- END TEST CASES ---

class Puzzle:
    def __init__(self):
        self.puzzle = []
        self.depth = 0
    # Creates puzzle from user input (taken from project manual example)
    # NOTE: does not scale, requires changes
    def createPuzzle(self, userRowOne, userRowTwo, userRowThree): 
        userRowOne = userRowOne.split()
        userRowTwo = userRowTwo.split()
        userRowThree = userRowThree.split()

        for i in range(3):
            userRowOne[i] = int(userRowOne[i])
            userRowTwo[i] = int(userRowTwo[i])
            userRowThree[i] = int(userRowThree[i])
        
        self.puzzle = [userRowOne, userRowTwo, userRowThree]
    def print_puzzle(self):
        for i in range(0, 3):
            print(self.puzzle[i], end="")
            print('\n', end="")

# Checks if two states are equal
def checkStateEquality(puzzle0: Puzzle, puzzle1: Puzzle):
    for i in len(puzzle0.puzzle):
        if not numpy.array_equal(puzzle0.puzzle[i], puzzle1.puzzle[i]): return False
    return True
