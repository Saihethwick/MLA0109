import itertools

def tsp(cities, start):
    n = len(cities)
    min_dist = float('inf')
    optimal_path = None

    # Generate all permutations of cities
    permutations = itertools.permutations(range(n))

    for path in permutations:
        if path[0] == start:
            dist = 0
            for i in range(n - 1):
                dist += cities[path[i]][path[i + 1]]
            dist += cities[path[-1]][path[0]]  # Return to starting city
            if dist < min_dist:
                min_dist = dist
                optimal_path = path

    return min_dist, optimal_path

# Example usage:
cities = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_city = 0
min_distance, optimal_path = tsp(cities, start_city)
print("Minimum distance:", min_distance)
print("Optimal path:", optimal_path)
