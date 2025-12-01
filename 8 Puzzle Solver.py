from queue import Queue

def is_goal(state):
    return state == [1,2,3,4,5,6,7,8,0]

def get_neighbors(state):
    moves = []
    zero_pos = state.index(0)
    swap_pos = []
    if zero_pos % 3 > 0: swap_pos.append(zero_pos-1) # left
    if zero_pos % 3 < 2: swap_pos.append(zero_pos+1) # right
    if zero_pos // 3 > 0: swap_pos.append(zero_pos-3) # up
    if zero_pos // 3 < 2: swap_pos.append(zero_pos+3) # down
    for pos in swap_pos:
        new_state = state[:]
        new_state[zero_pos], new_state[pos] = new_state[pos], new_state[zero_pos]
        moves.append(new_state)
    return moves

def bfs(initial_state):
    q = Queue()
    q.put([initial_state])
    visited = set()
    while not q.empty():
        path = q.get()
        state = tuple(path[-1])
        if state in visited: continue
        visited.add(state)
        if is_goal(list(state)):
            return path
        for neighbor in get_neighbors(list(state)):
            q.put(path + [neighbor])
    return None

init_state = [1,2,3,4,0,5,6,7,8]
solution = bfs(init_state)
for step in solution:
    print(step)