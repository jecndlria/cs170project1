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

def uniformCostSearch(puzzle: list[list[int]]):
    return 0

def misplacedTileHeuristic(puzzle: list[list[int]]):
    return 0

def manhattanDistanceHeuristic(puzzle: list[list[int]]):
    return 0