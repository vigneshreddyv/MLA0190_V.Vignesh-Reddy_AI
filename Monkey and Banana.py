# Q4: Monkey and Banana problem using BFS (state‑space search)

from collections import deque

# State: (monkey_pos, box_pos, monkey_on_box, has_banana)
# positions: 'door', 'center', 'window'

def get_actions(state):
    monkey_pos, box_pos, on_box, has_banana = state
    actions = []

    # 1. Move monkey alone
    for pos in ['door', 'center', 'window']:
        if pos != monkey_pos:
            actions.append(("Move monkey to " + pos,
                            (pos, box_pos, on_box if pos == box_pos else False, has_banana)))

    # 2. Push box (monkey and box move together) – only if monkey at box and not on box
    if monkey_pos == box_pos and not on_box:
        for pos in ['door', 'center', 'window']:
            if pos != box_pos:
                actions.append(("Push box to " + pos,
                                (pos, pos, False, has_banana)))

    # 3. Climb box
    if monkey_pos == box_pos and not on_box:
        actions.append(("Climb box", (monkey_pos, box_pos, True, has_banana)))

    # 4. Get banana (assume banana is hanging at center)
    if monkey_pos == 'center' and box_pos == 'center' and on_box and not has_banana:
        actions.append(("Grab banana", (monkey_pos, box_pos, on_box, True)))

    return actions

def bfs_monkey_banana():
    start = ('door', 'window', False, False)
    goal_has_banana = True

    q = deque()
    q.append((start, []))
    visited = set([start])

    while q:
        state, path = q.popleft()
        monkey_pos, box_pos, on_box, has_banana = state

        if has_banana == goal_has_banana:
            print("Solution found!")
            for step in path:
                print(step)
            print("Final state:", state)
            return

        for action, new_state in get_actions(state):
            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, path + [action]))

    print("No solution.")

if __name__ == "__main__":
    bfs_monkey_banana()