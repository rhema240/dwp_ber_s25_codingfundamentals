print("Task 1.")
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
print("scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]")
print("Sum of the list", sum(scores))

#Count the number of 3s on the list
counter = 0
for i in scores:
    if i== 3:
      counter = counter + 1
print("Number of 3s on the list is:",counter)

#Maximum number on the list
print("The Maximim number is:", max(scores))

#Turn into list to sets
print("Scores to sets", {5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12})

#3. Common Number on the list
print("Task 3.")
list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]
common_elements= set(list_1) & set(list_2)
print("Common elements:", list(common_elements))


#4.1 Goes thouogh each number on the list
print("Task 4.")
print("all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]")
all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
all_numbers.sort(reverse= True)
print(all_numbers)

#5. Reverse the list#
print("Task 5.")
reverse_this_list = [10, 20, 30, 40, 50]
reverse_this_list.reverse()
print(reverse_this_list)

#6. Convert Scores list from ex. 0 in a set and print its elements
print(scores)

#7. Create a list of tuples with 5 countries and capitals
countries_capitals= [("Nigeria, Abuja" , "Ghana, Accra" , "Cameroon, Yaounde", "Congo DRC, Kinshasa", "Egypt, Cairo")]
print(countries_capitals)