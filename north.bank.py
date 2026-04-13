import itertools
import math

# Coordinates extracted from the provided table
north_bank_locations = {
    "The Astana": (1.56362, 110.34554),
    "State Legislative Assembly Building": (1.56206, 110.34791),
    "Brooke Gallery": (1.56062, 110.34948)
}

def calculate_distance(point1, point2):
    """Calculates Euclidean distance between two coordinate pairs."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_shortest_path(locations):
    names = list(locations.keys())
    shortest_dist = float('inf')
    best_path = None

    # Conquer: Check all permutations for the small subset [cite: 37]
    for path in itertools.permutations(names):
        current_path_dist = 0
        for i in range(len(path) - 1):
            current_path_dist += calculate_distance(
                locations[path[i]], 
                locations[path[i+1]]
            )
        
        if current_path_dist < shortest_dist:
            shortest_dist = current_path_dist
            best_path = path
            
    return best_path, shortest_dist

# Execute the search
route, distance = find_shortest_path(north_bank_locations)

print("--- Optimized North Bank Route ---")
for i, spot in enumerate(route, 1):
    print(f"{i}. {spot}")

print(f"\nTotal Path Distance: {distance:.6f}")