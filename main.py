from datetime import datetime
import os
import puzzle
import sys
# import test cases
from puzzle import goalState, veryEasy, easy, doable, oh_boy, impossible, depth31, depth8, depth12, depth16, depth20
from search import generalSearch

def main():
    fileName = str(datetime.now())
    sys.stdout=open(f"output/{fileName}", "w")
    puzzlePrompt = input("This is an 8-Puzzle solver. Type \'0\' to use a default puzzle, or anything else to input your own puzzle.\n")
    if puzzlePrompt == '0':
        selectedDifficulty = input("Select the difficulty of the default puzzle from 0 to 9 (inclusive): ")
        if selectedDifficulty == '0':
            print("You have selected \'Trivial\'")
            userPuzzle = goalState
        if selectedDifficulty == '1':
            print("You have selected \'Very Easy\'")
            userPuzzle = veryEasy
        if selectedDifficulty == '2':
            print("You have selected \'Easy\'")
            userPuzzle = easy
        if selectedDifficulty == '3':
            print("You have selected \'Doable\'")
            userPuzzle = doable
        if selectedDifficulty == '4':
            print("You have selected \'Getting harder...\'")
            userPuzzle = depth8
        if selectedDifficulty == '5':
            print("You have selected \'Medium\'")
            userPuzzle = depth12
        if selectedDifficulty == '6':
            print("You have selected \'Hard\'")
            userPuzzle = depth16
        if selectedDifficulty == '7':
            print("You have selected \'Very Hard\'")
            userPuzzle = depth20
        if selectedDifficulty == '8':
            print("You have selected \'Oh, boy\'")
            userPuzzle = oh_boy
        if selectedDifficulty == '9':
            print("You have selected \'Impossible\'")
            userPuzzle = impossible
        else:
            print("Secret difficulty: Computer Crasher")
            userPuzzle = depth31
    else:
        print("Enter a valid 8-puzzle configuration by each row, using a \'0\' to represent the blank spot. Separate each number with a space, and press ENTER when you finish a row.")
        userRowOne = input("Enter Row #1: \n")
        userRowTwo = input("Enter Row #2: \n")
        userRowThree = input("Enter Row #3: \n")

        userPuzzle = puzzle.createPuzzle(userRowOne, userRowTwo, userRowThree)
    
    heuristic = input("Enter 0 to use Uniform Cost Search, 1 to use Misplaced Tile Heuristic, 2 to use Manhattan Distance Heuristic: \n")
    heuristic = int(heuristic)
    node = generalSearch(userPuzzle, heuristic)
    sys.stdout.close()
    if heuristic == 0:
        heuristicStr = "UniformCostSearch"
    if heuristic == 1:
        heuristicStr = "MisplacedTileHeuristic"
    if heuristic == 2:
        heuristicStr = "ManhattanDistanceHeuristic"
    depthStr = str(node.depth)
    os.rename(f"output/{fileName}", f"output/{heuristicStr}Depth{depthStr}on{fileName}")
    return

if __name__ == "__main__":
    main()