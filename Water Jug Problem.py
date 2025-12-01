# Q7: Water Jug problem using BFS
# example: jug A = 4L, jug B = 3L, goal = 2L in any jug

from collections import deque

def water_jug_bfs(capA, capB, goal):
    start = (0, 0)
    q = deque([(start, [])])
    visited = set([start])

    while q:
        (a, b), path = q.popleft()
        if a == goal or b == goal:
            print("Solution found:")
            for step in path:
                print(step)
            print("Final state:", (a, b))
            return

        next_states = []

        # 1. Fill A
        next_states.append(((capA, b), "Fill A"))
        # 2. Fill B
        next_states.append(((a, capB), "Fill B"))
        # 3. Empty A
        next_states.append(((0, b), "Empty A"))
        # 4. Empty B
        next_states.append(((a, 0), "Empty B"))
        # 5. Pour A -> B
        pour = min(a, capB - b)
        next_states.append(((a - pour, b + pour), "Pour A to B"))
        # 6. Pour B -> A
        pour = min(b, capA - a)
        next_states.append(((a + pour, b - pour), "Pour B to A"))

        for (na, nb), action in next_states:
            state = (na, nb)
            if state not in visited:
                visited.add(state)
                q.append((state, path + [f"{action}: ({na}, {nb})"]))

    print("No solution.")

if __name__ == "__main__":
    water_jug_bfs(4, 3, 2)