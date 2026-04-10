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

