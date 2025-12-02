# Problem 1: Min–Max on a small game tree

INF = 10**9

class Node:
    def __init__(self, value=None, children=None):
        self.value = value          # terminal value for leaf
        self.children = children or []

def minimax(node, depth, maximizing_player):
    if not node.children:          # leaf node
        return node.value

    if maximizing_player:
        best = -INF
        for child in node.children:
            val = minimax(child, depth + 1, False)
            best = max(best, val)
        return best
    else:
        best = INF
        for child in node.children:
            val = minimax(child, depth + 1, True)
            best = min(best, val)
        return best

if __name__ == "__main__":
    # Example tree:
    #          (root)
    #        /    \
    #      A        B
    #    / | \    / | \
    #   3  5  2  9  1  4
    A = Node(children=[Node(3), Node(5), Node(2)])
    B = Node(children=[Node(9), Node(1), Node(4)])
    root = Node(children=[A, B])

    result = minimax(root, 0, True)
    print("Min–Max value of root =", result)