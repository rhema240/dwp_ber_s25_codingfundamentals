european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                   ("Moscow", [12678079, "Borscht", "Red Square"]),
                   ("London", [8982000, "Fish and Chips", "Big Ben"]),
                   ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                   ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                   ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                   ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                   ("Paris", [2140526, "Croissant", "Eiffel Tower"])]

#1. Create an empty dictionary: `european_cities_info`
european_cities_info = {"": ""}

#2. Loop over the `european_cities` and unpack each tuple
#european_cities_info1 = []

european_cities_info2 = [european_cities]
print(european_cities_info2)  #still a tuple

#for city, code, food, place in european_cities():
#    european_cities_info1.append()
#    print(european_cities_info1.append)


#3. Print dictionary with the format City --> [Population, Dish, Landmark]

#sort list

#4. Sort the `european_cities_info` dictionary alphabetically by city (use sorted)

european_cities_info3 = []
for city in european_cities_info2:
    european_cities_info2.sort()
    print(european_cities_info2)


#5. Safely print the 'Berlin' info from the `european_cities_info` dictionary
#6. Safely print the type of 'London' from the `european_cities_info` dictionary
#7. Safely print 'Barcelona' from the `european_cities_info` dictionary or 'Not Found'
#8. Add new city `("Rome", [2870500, "Pasta", "Colosseum"])`
#9. Remove "Madrid" from `european_cities_info`
#10. Check to see if Amsterdam is in `european_cities_info` and print whether it is there or not

### Bonus: Create a dictionary from two lists:
#### Use the functions dict() and zip()
dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
