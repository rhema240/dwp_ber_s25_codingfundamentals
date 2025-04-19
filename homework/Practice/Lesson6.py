''''
def if_even(number):
    return number% 2 ==0

l = [1,2,3,4,5,6]
for n in l:
    if if_even(n):
        print(n)

#How use use a function and the user inputs
def add (a = input("Write a number:")):
    print(a)

add()
'''

#Ex1
quota = 10
value = int(input("Give a value:"))

if value>= 10:
    print("Done")
else:
    print("Not Done")

#Ex2
quota = 10
if value>= 10:
    print("0")
else:
    print(quota - value)

#Ex3
def fruits_remaining(fruits_picked,fruits_quota):
    if fruits_picked>=fruits_quota:
        print("0")
    else:
        print(fruits_quota - fruits_picked)

        return fruits_remaining

#Ex4
fruits_remaining(10,12)

#Bonus
def is_friday_off (fruits_picked, fruits_quota):
    value = fruits_picked == fruits_quota
    if value:
        print("Friday off")
    else:
        print("Not off")

#fruits_picked =[223,212,2002,234]
#fruits_quota = 880