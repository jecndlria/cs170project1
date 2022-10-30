class Node(object):
    def __init__(self, puzzle: list[list[int]]):
        self.puzzle = puzzle
        self.children = []
    def addChild(self, puzzle: list[list[int]]):
        self.children.append(puzzle)
