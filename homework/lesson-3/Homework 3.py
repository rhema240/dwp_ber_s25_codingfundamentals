#Number 1
print("Number Conversions")
number1 = input ("give a number:")
number2 = input ("give another number:")
convert1 = int(number1)
convert2 = int(number2)
print("addition",convert1+convert2)
print("subtraction", convert1-convert2)
print("mulipication",convert1*convert2)

#Number 2
number3 = int(input("Type a number:"))
if number3%3 != 1:
    print("Double the number is", number3 **2)

#Number 3
print("Finding if the number is odd or even")
number4 = int(input("give a number:"))
if number4% 2 == 0:
    print("The number is even")
else:
    print("The number is Odd")
    
#Number 4
print("Greater than or Less Than")
first_number= int(input("give a number:"))
second_number= int(input("give another number:"))
if first_number<second_number:
    print("the second number is greater")
elif first_number>second_number:
    print("the first number is greater")
else: 
    print("both numbers are the equal")


#Number 5
print("Print Numbers 1 to 10")
count= 1
while count <=10:
    print(count)
    count= count + 1

'''
#Number 6: 
print("Multiplication Table")
multi = int(input("Enter a number"))
for i in range (1,11)

'''
