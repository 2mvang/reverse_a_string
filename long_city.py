#Given: [{cities}]
# #=> : 3 longest name of cities []

def three_bigggest_named(cities):
    cities_arr = cities[0:2]
    for city in cities:
        char_count = len(city["name"])
        for c in cities_arr:
            if char_count > len(c["name"]) and c["name"] != city["name"]:
                c = city

print three_bigggest_named("Chicago","San Francisco","Detroit","Paris")
