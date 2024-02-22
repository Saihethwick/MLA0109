import random

def objective_function(state):
    # Example objective function: maximize the sum of values
    return sum(state)

def generate_neighbor(state):
    # Example neighbor generation: randomly change one element
    neighbor = state[:]
    index = random.randint(0, len(state) - 1)
    neighbor[index] = random.randint(0, 10)  # New random value
    return neighbor

def hill_climbing(max_iterations):
    # Generate a random initial solution
    current_state = [random.randint(0, 10) for _ in range(5)]
    current_value = objective_function(current_state)

    for _ in range(max_iterations):
        neighbor = generate_neighbor(current_state)
        neighbor_value = objective_function(neighbor)

        if neighbor_value > current_value:
            current_state = neighbor
            current_value = neighbor_value

    return current_state, current_value

# Example usage:
best_solution, best_value = hill_climbing(max_iterations=1000)
print("Best solution:", best_solution)
print("Best value:", best_value)
