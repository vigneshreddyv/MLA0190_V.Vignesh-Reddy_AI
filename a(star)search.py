# Problem 3: A* search on a graph

import heapq

def a_star_search(graph, start, goal, heuristic):
    # graph: dict node -> list of (neighbor, cost)
    open_set = []
    heapq.heappush(open_set, (0, start))  # (f, node)

    came_from = {}
    g_score = {start: 0}

    while open_set:
        f, current = heapq.heappop(open_set)

        if current == goal:
            # reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost
            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None, float("inf")

# Example: small graph and straight‑line heuristic (dummy values)
def heuristic(node, goal):
    h_values = {
        'S': 7, 'A': 6, 'B': 2, 'C': 1, 'G': 0
    }
    return h_values.get(node, 0)

if __name__ == "__main__":
    # Graph: (node: [(neighbor, cost), ...])
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('B', 2), ('C', 5)],
        'B': [('C', 1), ('G', 7)],
        'C': [('G', 3)],
        'G': []
    }

    path, cost = a_star_search(graph, 'S', 'G', heuristic)
    print("Optimal path:", path)
    print("Total cost:", cost)