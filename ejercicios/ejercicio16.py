# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# planets.append("Pluto")
# number_of_planets = len(planets)
# # print(f"There are actually, {number_of_planets,} planets in the solar system.")
# print("The first planet is", planets[0])


# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# planets_before_earth = planets[0:20:2]
# print(planets_before_earth)


rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1