# Homework L7: Shopping List
#Question: Create a program that:
'''
1. Asks users to enter items for their shopping list
2. Keeps asking for items until they type 'done' 
3. Shows the complete list at the end
'''

print("Let's Make your Shopping List\n")

shopping_list = [] 

while True:
    item = input("Enter an item (or type 'done' to finish): ")

    if item.lower() == "done":
        print("\nYour shopping list is ready!")
        print("Items in your list:")
        for i, list_item in enumerate(shopping_list, start=1):
            print(f"{i}. {list_item}")
        print(f"\nTotal items: {len(shopping_list)}")
        break
    else:
        shopping_list.append(item)
        print("Item added! Add more or type 'done' to finish.\n")



'''
## REQUIREMENTS
### The program must:
1. Use a while loop
2. Store items in a list
3. Be case-insensitive for the word 'done' (DONE, Done, done should all work)
4. Number the items when displaying the final list
5. Show the total number of items at the end


### Input handling:
1. Ignore empty inputs (just ask again)
2. Remove extra spaces before and after items
3. Don't add 'done' to the shopping list


## TESTING YOUR PROGRAM
Test your program with these scenarios:

1. Normal items: milk, bread, eggs
2. Items with spaces: " milk  " (extra spaces)
3. Empty inputs: (just press Enter)
4. Different cases of 'done': DONE, Done, done
5. Single item then done
6. Directly typing 'done' (empty list)

## BONUS CHALLENGES (OPTIONAL)
After completing the basic requirements, try these:

1. Don't allow duplicate items
2. Sort the list alphabetically before displaying

'''