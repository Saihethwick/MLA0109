import heapq

class Node:
    def __init__(self, state, parent=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = h_cost

    def f_cost(self):
        return self.g_cost + self.h_cost

    def __lt__(self, other):
        return self.f_cost() < other.f_cost()


def astar(start_state, goal_state, heuristic, successors):
    open_list = []
    closed_set = set()

    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_list, (start_node.f_cost(), start_node))

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for successor, cost in successors(current_node.state):
            if successor in closed_set:
                continue

            g_cost = current_node.g_cost + cost
            h_cost = heuristic(successor, goal_state)
            new_node = Node(successor, current_node, g_cost, h_cost)
            heapq.heappush(open_list, (new_node.f_cost(), new_node))

    return None  # No path found

# Example usage:
def heuristic(state, goal_state):
    # Manhattan distance heuristic
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

def successors(state):
    x, y = state
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(candidate, 1) for candidate in candidates if 0 <= candidate[0] < 5 and 0 <= candidate[1] < 5]

start_state = (0, 0)
goal_state = (4, 4)
path = astar(start_state, goal_state, heuristic, successors)
print("Path:", path)
