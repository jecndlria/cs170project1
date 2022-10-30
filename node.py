class Node(object):
    def __init__(self, puzzle: list[list[int]]):
        self.puzzle = puzzle
        self.children = []
        self.depth = 0
        self.priceOfNode = 0

    # __lt__() is the dunder function that can be overloaded for classes
    # Needed for the heap, so it knows to prioritize based on node price.
    def __lt__(self, node):
        return self.priceOfNode < node.priceOfNode