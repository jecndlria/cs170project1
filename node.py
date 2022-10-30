class Node(object):
    def __init__(self, puzzle: list[list[int]]):
        self.puzzle = puzzle
        self.children = []
        self.depth = 0
        self.priceOfNode = 0

    def __lt__(self, node):
        return self.priceOfNode < node.priceOfNode

    def addChild(self, node):
        self.children.append(node)
        
    def setDepth(self, depth):
        self.depth = depth