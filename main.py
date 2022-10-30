import puzzle, search
from node import Node

# import test cases
from puzzle import goalState, veryEasy, easy, doable, oh_boy, impossible
from search import expandNode
import copy

def main():
    # puzzlePrompt = input("This is an 8-Puzzle solver. Type \'0\' to use a default puzzle, or anything else to input your own puzzle.\n")
    # if puzzlePrompt == '0':
    #     selectedDifficulty = input("Select the difficulty of the default puzzle from 0 to 5 (inclusive): ")
    #     if selectedDifficulty == '0':
    #         print("You have selected \'Trivial\'")
    #         userPuzzle = goalState
    #     if selectedDifficulty == '1':
    #         print("You have selected \'Very Easy\'")
    #         userPuzzle = veryEasy
    #     if selectedDifficulty == '2':
    #         print("You have selected \'Easy\'")
    #         userPuzzle = easy
    #     if selectedDifficulty == '3':
    #         print("You have selected \'Doable\'")
    #         userPuzzle = doable
    #     if selectedDifficulty == '4':
    #         print("You have selected \'Oh, boy\'")
    #         userPuzzle = oh_boy
    #     if selectedDifficulty == '5':
    #         print("You have selected \'Impossible\'")
    #         userPuzzle = impossible
    # else:
    #     print("Enter a valid 8-puzzle configuration by each row, using a \'0\' to represent the blank spot. Separate each number with a space, and press ENTER when you finish a row.")
    #     userRowOne = input("Enter Row #1: ")
    #     userRowTwo = input("Enter Row #2: ")
    #     userRowThree = input("Enter Row #3: ")

    #     userPuzzle = puzzle.createPuzzle(userRowOne, userRowTwo, userRowThree)
    print(search.manhattanDistanceHeuristic([[3,2,8],[4,5,6],[7,1,0]]))
    print(search.manhattanDistanceHeuristic(oh_boy))
    expandNode(Node(doable))

    object1 = Node(goalState)
    object2 = Node(copy.deepcopy(goalState))

    object1 = str(object1.puzzle)
    object2 = str(object2.puzzle)

    print(hash(object1))
    print(hash(object2))

    return

if __name__ == "__main__":
    main()