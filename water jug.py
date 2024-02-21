from collections import deque

# Define the capacity of the jugs
jug_capacity = (4, 3)

# Define the initial state and the goal state
initial_state = (0, 0)
goal = 2

def pour(state, from_jug, to_jug):
    state = list(state)
    amount_poured = min(state[from_jug], jug_capacity[to_jug] - state[to_jug])
    state[from_jug] -= amount_poured
    state[to_jug] += amount_poured
    return tuple(state)

def is_valid(state):
    return 0 <= state[0] <= jug_capacity[0] and 0 <= state[1] <= jug_capacity[1]

def solve_water_jug():
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state[0] == goal:
            print("Solution found:", path)
            return

        visited.add(current_state)

        for action, action_name in [(0, "Fill 4-gallon jug"),
                                    (1, "Fill 3-gallon jug"),
                                    (0, "Pour from 4-gallon jug to 3-gallon jug"),
                                    (1, "Pour from 3-gallon jug to 4-gallon jug"),
                                    (0, "Empty 4-gallon jug"),
                                    (1, "Empty 3-gallon jug")]:
            new_state = pour(current_state, action, 1 - action)
            if new_state not in visited and is_valid(new_state):
                queue.append((new_state, path + [action_name]))
                visited.add(new_state)

    print("No solution found.")

# Solve the water jug problem
solve_water_jug()
