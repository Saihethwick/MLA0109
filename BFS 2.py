from queue import PriorityQueue

def best_first_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        cost, node = queue.get()
        visited.add(node)

        if node == goal:
            return True

        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in visited:
                queue.put((neighbor_cost, neighbor))

    return False

# Example usage:
graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('E', 4)],
    'D': [('F', 3)],
    'E': [],
    'F': []
}
start = 'A'
goal = 'F'

if best_first_search(graph, start, goal):
    print("Goal reached")
else:
    print("Goal not reachable")
