from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            order.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
    print("BFS order:", order)

graph = {0:[1,2], 1:[3,4], 2:[], 3:[], 4:[]}
bfs(graph, 0)