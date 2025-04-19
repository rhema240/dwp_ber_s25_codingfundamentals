#Average of numbers
#Example1
import statistics
numbers = [10, 20, 30, 40, 50]
average = statistics.mean(numbers)
print("Average:", average)

#Example2
average = sum(numbers) / len(numbers)
print("Average:", average)