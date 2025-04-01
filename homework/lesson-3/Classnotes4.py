#Learnings on Lists
'''
fruits = ['apple', 'mango', 'orange']
print(fruits)
#This would show the 1 index of the list which is mango
#print(fruits(1))
#Adds pinapple to the list wehn printed
fruits.append('pineapple')
print(fruits)

#Remove x in this case apple from the list
fruits.remove('apple')
print()

#Insert at index 2 banana
fruits.insert(2,'banana')
print(fruits.insert)

#Arange the elements in ascending order
fruits.sort()
print(fruits)

#len- how many elemnts are in the elements of fruits
print(len(fruits))

#example to sort 
scores = (1, 5, 345, 367, 9, 52)
scores.sort()

print(scores)'
'''

#Sets
#How to define a set, sets do not allow duplicates but lists do, so if in the groceries list we add tomoates twice it would remove the duplicate
groceries = set{}

#example
groceries1 = {'tomatoes, '}
print(groceries)

#Tuples cannot change but can be duplictes, you can tremove or add
