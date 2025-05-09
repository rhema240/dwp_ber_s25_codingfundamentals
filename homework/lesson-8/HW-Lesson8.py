european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                   ("Moscow", [12678079, "Borscht", "Red Square"]),
                   ("London", [8982000, "Fish and Chips", "Big Ben"]),
                   ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                   ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                   ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                   ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                   ("Paris", [2140526, "Croissant", "Eiffel Tower"])]

#1. Create an empty dictionary: `european_cities_info`
european_cities_info = {}

#2. Loop over the `european_cities` and unpack each tuple
print("Step 2. \n")
for city, attributes in european_cities:
    european_cities_info[city] = {
        "population": attributes[0],
        "dish": attributes[1],
        "landmark": attributes[2]
    }

print(european_cities_info)

print("..\n")

#4. Sort the `european_cities_info` dictionary alphabetically by city (use sorted)
print("Step 4. \n")
sorted_european_cities_info = dict(sorted(european_cities_info.items()))

print(sorted_european_cities_info)

print("..\n")

#5. Safely print the 'Berlin' info from the `european_cities_info` dictionary
print("Step 5. \n")
berlin_info = european_cities_info.get('Berlin')
print(berlin_info)

print("..\n")

#6. Safely print the type of 'London' from the `european_cities_info` dictionary
print("Step 6. \n")
london_info =european_cities_info.get('London')
print(london_info)

print("..\n")

#7. Safely print 'Barcelona' from the `european_cities_info` dictionary or 'Not Found'
print("Step 7. \n")
if "Barcelona" in european_cities_info:
    print(european_cities_info.get('Barcelona'))
else:
    print("Not Found")

print("..\n")

#8. Add new city
#new_list = european_cities_info[Rome].append([2870500, "Pasta", "Colosseum"])
#print(new_list)
print("Step 8. \n")
european_cities_info["Rome"] = {
    "population": 2870500,
    "dish": "Pasta",
    "landmark": "Colosseum"
}
print(european_cities_info)

print("..\n")

#9. Remove "Madrid" from `european_cities_info`


#10. Check to see if Amsterdam is in `european_cities_info` and print whether it is there or not
print("Step 10. \n")
if "Amsterdam" in european_cities_info:
    print(european_cities_info.get("Amsterdam"))
else:
    print("Not Found")

print("..\n")

### Bonus: Create a dictionary from two lists:
#### Use the functions dict() and zip()
dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]


