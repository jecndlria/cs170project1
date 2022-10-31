# Why I'm using a Node object to create the game tree:
    # Makes it easy to keep track of the children, depth, and price of node
    # Easy to expand (push results of expand function to self.children)
class Node(object):
    def __init__(self, puzzle: list[list[int]]):
        self.puzzle = puzzle
        self.children = []
        self.depth = 0
        self.priceOfNode = 0

    # __lt__() is the dunder function that can be overloaded for classes
    # Needed for the heapq, so it knows to prioritize based on node price.
        # (taken from heapq documentation)
    def __lt__(self, node):
        return self.priceOfNode < node.priceOfNode