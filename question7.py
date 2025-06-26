# Calculate the factorial of a number using lambda function.

# Using reduce function from functools to calculate factorial of given number by lambda function
from functools import reduce

num = 0
try:
    num = int(input("Enter the number: "))
except:
    print("Please provide a valid input. Exiting...")
    exit(1)

if(num < 0):
    print("Factorial is not defined for negative values. Exiting...")
    exit(1)

print(f"The factorial of number {num} is {reduce(lambda x,y: x*y, range(1, num+1), 1)}")
