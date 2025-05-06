#Dictionary
#Excerise 1
## 1. Create a dictionary with you personal info: name, age, occupation
print("My first dictionary\n")
print("Exercise 1. ")
my_info ={"name":"Rhema",  
       "nationality":"nigerian",
       "occupation":"student",
       "age":22, 
       "height":5.5, 
       "colour":"Lila"}

## 2. Add your hobby to the dictionary
print("Add my hobbies to info\n")
my_info["hobbies"] = ["painting", "drawing", "sewing","reading"]
print(my_info)

## 3. Print your occupation (two versions: calling the key and using get() )
print(".................................\n")

print("Get occupation")
print("using get function:", my_info.get("occupation"))
print("using brackets:", my_info["occupation"])

## 4. Print your Nationality (two versions: calling the key and using get() with parameter )
print(".................................\n")
print("Get Nationality")
print(my_info.get("nationality"))


## 5. Print your Nationality, if not found print “Unknown”
if "nationality" in my_info:
    print(my_info.get("nationality"))
else:
    print("unknown")

## 6. Print only the keys of the dictionary
print(".................................\n")
print("Get Keys")
print(my_info.keys())

## 7. Print only the values of the dictionary
print(".................................\n")
print("Get Values")
print(my_info.values())

## 8. Update your occupation
print(".................................\n")
print("Change occupation")
my_info["occupation"] = "analyst"
print(my_info)

## 9. Remove your age from the dictionary
print(".................................\n")
print("Take age out")
my_info.pop("age")
print(my_info)

## 10. Check if the key "Favorite Color" is in the dictionary
if "favorite_colour" in my_info:
     print(my_info.get("favorite_colour"))

else:
     print("your favorite coulour is not on dictionary")

#Add to the dictionary
print(".................................\n")
my_info["hobbies"].append("cooking")
print(my_info.get("hobbies"))


#Excerise 2.
print(".................................\n")

print(".................................\n")
print("Exercise 2. ")

my_dict = {"name": "Rapunzel", "age": 19, "hobbies": ["painting", "singing", "reading"] }

print("Keys are: ")
for key in my_dict.keys():
     print(key)

print(".................................\n")

print("Values: ")
for value in my_dict.values():
     print(value)

print(".................................\n")

print("Items in the dictionary: ")
for k, v in my_dict.items():
     print(k, "------>", v)

print(".................................\n")

## Exercise 2.1
 ##From the dictionary below, calculate the total household income:
print("Exercise 2.")
incomes = {"Adult 1": 3600.00, "Adult 2": 2500.00, "Children": 500.00 }

acc = 0
for income in incomes.values():
   sum = acc + income
print(sum)
    
print(".................................\n")    

## Exercise 2.2
print("Exercise 2.2")
# convert the dictionary into a list of tuples using a for loop. ( hint: use the method append())
my_list = []

for k,v in my_dict.items():
     my_list.append((k,v))
print(my_list.append)

print(".................................\n")

## Exercise 2.3
print("Excerise 2.3 ")
## Create dictionaries similar to the Rapunzel one for you and 2 of your friends. 
my_dict = {"name": "Rhema", "age": 22, "hobbies": ["painting", "singing", "reading"] }
my_friend = {"name": "Christa", "age": 23, "hobbies": ["drawing", "reading", "sleeping"]}

## Create a list of dictionaries  with both information 
our_list = [my_dict, my_friend]

## Calculate the average of all your ages.

total_sum = 0
for dictionary in our_list:
     total_sum = total_sum + dictionary.get("age")

average = total_sum/ len(our_list)
print("Average Age", average)



#NOTES
#adding items
#["occupation":"engineer"]

#how to retrieve values
#info.values

#to get items
#info.items

#to reomove key pair
#info.pop("occupation")

