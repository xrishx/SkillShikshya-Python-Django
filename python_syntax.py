# Basic Data Types

age = 12                # int
height = 5.9            # float
name = "Alice"          # string
is_student = True       # boolean

# Complex Data Types

# Lists: Ordered, mutable and allows duplicates
fruits = ["apple", "orange", "banana"]

# Tuple: Ordered, immutable and allows duplicates
coordinates = (10 , 20)

# Set: Unordered, no duplicates
unique_numbers = {1, 2, 3, 4}

# Dictionary: Key:Value pairs, mutable and no duplicates
# Ordered in ver3.7, unordered in earlier versions
person = {"name":"Alice", "age":25}

# Control Structures

# Conditionals
if age > 18:
    print("Adult")
elif age == 18:
    print("Just became an adult")
else:
    print("Minor")

# For Loop
for i in range(5):      # iterates from 0 to 4
    print(f"Number: {i}")

# While loop
count = 0 
while count < 0:
    print("Counting:", count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

# Function Call
n =input("Enter your name: ")
print(greet(n))

