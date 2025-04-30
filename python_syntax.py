# Basic Data Types
age = 12                # int
height = 5.9            # float
name = "Alice"          # string
is_student = True       # boolean

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

