# Homework L7: Shopping List
#Question: Create a program that:

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
## TESTING YOUR PROGRAM
Test your program with these scenarios:

1. Normal items: milk, bread, eggs
2. Items with spaces: " milk  " (extra spaces)
3. Empty inputs: (just press Enter)
4. Different cases of 'done': DONE, Done, done


## BONUS CHALLENGES (OPTIONAL)
After completing the basic requirements, try these:

1. Don't allow duplicate items
2. Sort the list alphabetically before displaying

'''