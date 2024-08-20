capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin",]
}


# Print Lille
print(travel_log["France"][1])


nested_list = ["A", "B", ["C", "D"]]

# Print D
print(nested_list[2][1])


new_travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}


# Print Stuttgart from new log
print(new_travel_log["Germany"]["cities_visited"][2])