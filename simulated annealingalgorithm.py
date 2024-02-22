import numpy as np
import math
import random

# Define the objective function (you can replace this with your own function)
def objective_function(x):
    return np.sin(x) + np.sin(0.5 * x)

# Define the simulated annealing function
def simulated_annealing(objective_function, initial_solution, initial_temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    best_solution = current_solution
    best_energy = current_energy

    for i in range(num_iterations):
        # Decrease temperature
        temperature = initial_temperature * math.exp(-cooling_rate * i)

        # Generate a random neighboring solution
        neighbor = current_solution + random.uniform(-1, 1)

        # Calculate energy difference
        neighbor_energy = objective_function(neighbor)
        energy_diff = neighbor_energy - current_energy

        # Accept or reject the neighbor
        if energy_diff < 0 or random.uniform(0, 1) < math.exp(-energy_diff / temperature):
            current_solution = neighbor
            current_energy = neighbor_energy

        # Update the best solution
        if current_energy < best_energy:
            best_solution = current_solution
            best_energy = current_energy

    return best_solution, best_energy

# Set initial parameters
initial_solution = 0  # Initial solution
initial_temperature = 100  # Initial temperature
cooling_rate = 0.01  # Cooling rate
num_iterations = 1000  # Number of iterations

# Run simulated annealing
best_solution, best_energy = simulated_annealing(objective_function, initial_solution, initial_temperature, cooling_rate, num_iterations)

# Print results
print("Best solution:", best_solution)
print("Best energy:", best_energy)
