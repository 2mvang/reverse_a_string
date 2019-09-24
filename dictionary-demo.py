def people_over_18(people):
    adults = []
    #loop
    for p in people:
    #check
        if p["age"] >= 18:
    #add to adults list
            adults.append(p)
    return adults

p = [
    {"name":"Abe", "age": 16},
    {"name":"June", "age": 21},
    {"name":"Jack", "age": 10},
    {"name":"Abi", "age": 21},
]

print (people_over_18(p))
