# Q6: DFS on a graph

def dfs_graph(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=" ")
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_graph(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: []
    }
    print("DFS order:", end=" ")
    dfs_graph(graph, 1)
    print()