import math

# The exact latitude and longitude for the Kuching attractions
south_bank = {
    "Sheraton Hotel": (1.55657, 110.35310),
    "Kuching Waterfront": (1.56048, 110.34577),
    "India Street": (1.55961, 110.34351),
    "Carpenter Street": (1.55827, 110.34596),
    "Borneo Cultures Museum": (1.55550, 110.34239),
    "Chinese History Museum": (1.55763, 110.34873)
}

north_bank = {
    "The Astana": (1.56362, 110.34554),
    "State Legislative Assembly Building": (1.56206, 110.34791),
    "Brooke Gallery": (1.56062, 110.34948)
}

# The Haversine formula to calculate true distance and vehicle travel time
def calculate_distance_and_time(coord1, coord2, vehicle_speed_kmh):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    radius = 6371.0 

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat / 2)**2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * (math.sin(dlon / 2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance_km = radius * c
    time_minutes = (distance_km / vehicle_speed_kmh) * 60
    
    return distance_km, time_minutes

# South Bank Route
# Nearest-neighbour heuristic starting from Sheraton Hotel.
# Visits all 6 South Bank locations and ends at Kuching Waterfront
def south_bank_route(vehicle_speed_kmh=60):
    """
    Finds an efficient South Bank route using the nearest-neighbour heuristic.

    Parameters:
        vehicle_speed_kmh (float): Assumed travel speed in km/h. Default is 60 km/h.

    Returns:
        route        (list of str)   : Ordered list of location names visited.
        total_dist   (float)         : Total route distance in kilometres.
        total_time   (float)         : Total estimated travel time in minutes.
        leg_details  (list of dict)  : Per-leg breakdown (from, to, distance, time).
    """

    START = "Sheraton Hotel"

    # Separate the starting point from the remaining stops to visit
    unvisited = {name: coord for name, coord in south_bank.items() if name != START}

    current_location = START
    current_coord    = south_bank[START]

    route       = [START]
    leg_details = []
    total_dist  = 0.0
    total_time  = 0.0

    # Nearest-neighbour: always move to the closest unvisited location
    while unvisited:
        nearest_name = None
        nearest_dist = float("inf")
        nearest_time = 0.0

        for name, coord in unvisited.items():
            dist, time = calculate_distance_and_time(current_coord, coord, vehicle_speed_kmh)
            if dist < nearest_dist:
                nearest_dist = dist
                nearest_time = time
                nearest_name = name

        # Record this leg
        leg_details.append({
            "from":     current_location,
            "to":       nearest_name,
            "distance_km":   round(nearest_dist, 4),
            "time_minutes":  round(nearest_time, 2)
        })

        total_dist += nearest_dist
        total_time += nearest_time

        # Move to the chosen location
        route.append(nearest_name)
        current_coord    = unvisited.pop(nearest_name)
        current_location = nearest_name

    return route, round(total_dist, 4), round(total_time, 2), leg_details
