# Problem 2: Alpha–Beta pruning with list of pruned leaf indices

INF = 10**9

class ABNode:
    def __init__(self, value=None, children=None, name=""):
        self.value = value
        self.children = children or []
        self.name = name            # for debugging / display

pruned_leaves = []                  # collect pruned leaf names

def alphabeta(node, depth, alpha, beta, maximizing_player):
    global pruned_leaves

    if not node.children:          # leaf node
        return node.value

    if maximizing_player:
        value = -INF
        for child in node.children:
            value = max(value, alphabeta(child, depth + 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                # remaining children of this node are pruned
                idx = node.children.index(child) + 1
                for rest in node.children[idx:]:
                    collect_pruned(rest)
                break
        return value
    else:
        value = INF
        for child in node.children:
            value = min(value, alphabeta(child, depth + 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                idx = node.children.index(child) + 1
                for rest in node.children[idx:]:
                    collect_pruned(rest)
                break
        return value

def collect_pruned(node):
    """Store names of all pruned leaves under this node."""
    if not node.children:
        pruned_leaves.append(node.name)
        return
    for ch in node.children:
        collect_pruned(ch)

if __name__ == "__main__":
    # Example same structure but with names for identification
    A = ABNode(name="A", children=[
        ABNode(3, name="A1"),
        ABNode(5, name="A2"),
        ABNode(2, name="A3")
    ])
    B = ABNode(name="B", children=[
        ABNode(9, name="B1"),
        ABNode(1, name="B2"),
        ABNode(4, name="B3")
    ])
    root = ABNode(name="Root", children=[A, B])

    value = alphabeta(root, 0, -INF, INF, True)
    print("Alpha–Beta value of root =", value)
    print("Pruned leaves:", pruned_leaves)