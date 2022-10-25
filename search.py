import anytree

visitedStates = {}
currentDepth = 0
nodesExpanded = 0
maxQueueSize = 0

def generalSearch(puzzle: list[list[int]], heuristic):
    return 0

# Intuition behind checking the legal moves: Depends on location of '0'
    # If in the middle, then 4 legal moves.
    # If in the miiddle of a row or column, then 3 legal moves.
    # If in corner, then 2 legal moves.

# A legal move is simply to swap the '0' with any adjacent element on the board.
def checkLegalOperations(puzzle: list[list[int]]):
    return 0

# Intuition behind the Misplaced Tile Heuristic:
    # It is trivial to search by row, since the goal of the puzzle is to sort each row in ascending order.
    # This makes it so we can easily keep track of what number should be where using an incremented variable.

# Thus, the algorithm is as follows:
    # 1. Initialize the variable "currentValue", which keeps track of the number that should be in the spot we look at.
        # Initialize the variable "misplacedTiles", which keeps track of how many misplaced tiles we have seen thus far.
    # 2. Iterate through the puzzle using a nested for loop. We will be searching each row from left to right... 
        # ...which will make it so we will search the entire game board in (what should be) ascending order.
    # 3. If the current value you see is not the blank (0), and it doesn't match the currentValue, increment misplacedTiles
    # 4. Increment currentValue.
    # 5. Terminate when you search the whole board and return misplacedTiles
# This also easily scales up to larger puzzle sizes.
def misplacedTileHeuristic(puzzle: list[list[int]]):
    currentValue = 1
    misplacedTiles = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != 0 and puzzle[i][j] != currentValue:
                misplacedTiles += 1
            currentValue += 1
    return misplacedTiles

# Intuition behind Manhattan Distance Heuristic:
    # As seen in the misplaced tile heuristic, it is straightforward to find the actual misplaced tiles.
    # However, in this heuristic, we must now find how many spaces the actual blocks are displaced.
    # In order to find how far displaced a block is, we must find how many rows and columns away the block is.
        # The sum of this displacement is the total displacement, since diagonal moves are not legal.
        # 0 0 8
        # 0 0 0
        # 0 0 0
        # In this example, the 8 is two rows, and one column away. The total displacement is 2 + 1 = 3 blocks.
    # The problem becomes trivial once we realize that we can simply take the ordered pair of the location of the misplaced block...
        # .. and the ordered pair of where it should be, and take the displacement by simply doing some (absolute value) subtraction.
    # How do we find the misplaced blocks? Use the algorithm defined in the misplaced tile heuristic!
def manhattanDistanceHeuristic(puzzle: list[list[int]]):
    return 