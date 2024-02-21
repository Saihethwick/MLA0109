def is_valid(state):
    # Check if the number of cannibals exceeds the number of missionaries on either side
    if state[0] > state[1] or state[2] > state[3]:
        return False
    # Check if the number of cannibals is greater than the number of missionaries in the boat
    if abs(state[0] - state[1]) > 2 or abs(state[2] - state[3]) > 2:
        return False
    return True

def solve_river_crossing():
    # Initial state: 3 missionaries, 3 cannibals on the left side, 0 on the right side
    initial_state = (3, 0, 3, 0)
    # Final state: 0 missionaries, 0 cannibals on the left side, 3 on the right side
    final_state = (0, 0, 0, 3)
    # Stack to store the states to be explored
    stack = [(initial_state, '')]
    # Set to store the visited states
    visited = set()
    while stack:
        state, moves = stack.pop()
        if state == final_state:
            print(f"Solution found: {moves}")
            return
        if state not in visited:
            visited.add(state)
            # Generate all possible next states
            for i in range(2):
                for j in range(2):
                    next_state = (state[0] - i, state[1] + i, state[2] - j, state[3] + j)
                    if is_valid(next_state):
                        stack.append((next_state, moves + f"M{'E' if i == 1 else 'W'}{'C' if j == 1 else 'W'}"))

solve_river_crossing()
