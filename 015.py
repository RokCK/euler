# Problem 015: Lattice Paths
import math

def num_paths(grid_size):
    return math.factorial(2*grid_size) // (math.factorial(grid_size)**2)

print(num_paths(20))
