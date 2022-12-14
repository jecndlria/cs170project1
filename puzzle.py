import numpy

# Creates puzzle from user input (taken from project manual example)
# NOTE: does not scale, requires changes
def createPuzzle(userRowOne, userRowTwo, userRowThree): 
    userRowOne = userRowOne.split()
    userRowTwo = userRowTwo.split()
    userRowThree = userRowThree.split()

    for i in range(len(userRowOne)):
        userRowOne[i] = int(userRowOne[i])
        userRowTwo[i] = int(userRowTwo[i])
        userRowThree[i] = int(userRowThree[i])

    puzzle = [userRowOne, userRowTwo, userRowThree]
    return puzzle
    
# Checks if two states are equal
def checkStateEquality(puzzle0: list[list[int]], puzzle1: list[list[int]]):
    for i in range(3):
        if not numpy.array_equal(puzzle0[i], puzzle1[i]): return False
    return True

def printPuzzle(puzzle: list[list[int]]):
    for i in range(0, 3):
        print(puzzle[i], end="")
        print('\n', end="")

# --- BEGIN TEST CASES ---
# Depth 0
goalState = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]

# Depth 1
veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]

# Depth 2
easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

# Depth 4
doable = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]

# Depth 8
depth8 = [[1, 3, 6],
          [5, 0, 2],
          [4, 7, 8]]

# Depth 12
depth12 = [[1, 3, 6],
           [5, 0, 7],
           [4, 8, 2]]

# Depth 16
depth16 = [[1, 6, 7],
           [5, 0, 3],
           [4, 8, 2]]
# Depth 20
depth20 = [[7, 1, 2],
           [4, 8, 5],
           [6, 3, 0]]

# Depth 22
oh_boy = [[8, 7, 1],
          [6, 0, 2],
          [5, 4, 3]]

# Depth 24
impossible = [[0, 7, 2],
              [4, 6, 1],
              [3, 5, 8]]

# Depth 31
depth31 = [[8, 6, 7],
           [2, 5, 4],
           [3, 0, 1]]

# --- END TEST CASES ---