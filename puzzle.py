# --- BEGIN TEST CASES ---

trivial = [[1, 2, 3],
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

eight_goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

# --- END TEST CASES ---

def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
        print('\n')

def createPuzzle(userInput): 
    return 0
