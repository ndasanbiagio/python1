def rocket_parts():
    print("payload, propellant, structure")
    
rocket_parts()

output = rocket_parts()

def rocket_parts():
    return "payload, propellant, structure"
output = rocket_parts()
output

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
distance_from_earth("Moon")

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

days_to_complete(238855, 75)