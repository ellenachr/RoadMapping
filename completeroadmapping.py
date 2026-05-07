import math
import itertools

locations = {
    # South Bank
    "Sheraton Hotel": (1.55657, 110.35310),
    "Kuching Waterfront": (1.56048, 110.34577),
    "India Street": (1.55961, 110.34351),
    "Carpenter Street": (1.55827, 110.34596),
    "Borneo Cultures Museum": (1.55550, 110.34239),
    "Chinese History Museum": (1.55763, 110.34873),
    # North Bank
    "The Astana": (1.56362, 110.34554),
    "State Legislative Assembly Building": (1.56206, 110.34791),
    "Brooke Gallery": (1.56062, 110.34948)
}

# We are using the Haversine formula as it is the accurate way to measure GPS coordinates.
def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    radius = 6371.0 # Earth's radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat / 2)**2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * (math.sin(dlon / 2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return radius * c # Returns distance in kilometers

def south_bank_route():
    start_point = "Sheraton Hotel"
    
    south_bank_stops = ["Kuching Waterfront", "India Street", "Carpenter Street", 
                        "Borneo Cultures Museum", "Chinese History Museum"]
    
    unvisited = {name: locations[name] for name in south_bank_stops}
    current_location = start_point
    current_coord = locations[start_point]

    route = [start_point]

    # Nearest-Neighbor Heuristic
    while unvisited:
        nearest_name = None
        nearest_dist = float("inf")

        for name, coord in unvisited.items():
            # USING ELL'S MATH ENGINE
            dist = calculate_distance(current_coord, coord) 
            if dist < nearest_dist:
                nearest_dist = dist
                nearest_name = name

        route.append(nearest_name)
        current_coord = unvisited.pop(nearest_name)

    return route

def north_bank_route():
    north_bank_stops = ["The Astana", "State Legislative Assembly Building", "Brooke Gallery"]
    shortest_dist = float('inf')
    best_path = None

    # Brute-force all combinations for the small subset
    for path in itertools.permutations(north_bank_stops):
        current_path_dist = 0
        for i in range(len(path) - 1):
            # USING ELL'S MATH ENGINE
            current_path_dist += calculate_distance(locations[path[i]], locations[path[i+1]])
        
        if current_path_dist < shortest_dist:
            shortest_dist = current_path_dist
            best_path = list(path)
            
    return best_path

def master_tour():
    print("=== KUCHING OPTIMIZED TOURISM ROUTE ===")
    
    sb_route = south_bank_route()
    nb_route = north_bank_route()
    
    if nb_route[0] != "The Astana":
        nb_route.reverse()
    
    full_route = sb_route + nb_route
    
    total_distance = 0.0
    for i in range(len(full_route) - 1):
        total_distance += calculate_distance(locations[full_route[i]], locations[full_route[i+1]])

    # Print the final output for the report
    print("\n--- LEG 1: SOUTH BANK ---")
    for i, spot in enumerate(sb_route):
        print(f"{i + 1}. {spot}")
        
    print("\n--- THE RIVER CROSSING ---")
    print(f"🚗  Drive across the bridge from {sb_route[-1]} across to {nb_route[0]}")

    print("\n--- LEG 2: NORTH BANK ---")
    for i, spot in enumerate(nb_route):
        print(f"{len(sb_route) + i + 1}. {spot}")
        
    print("\n=== FINAL ITINERARY DETAILS ===")
    print(f"Total Attractions: {len(full_route)}")
    print(f"Total Travel Distance: {total_distance:.2f} km")

if __name__ == '__main__':
    master_tour()