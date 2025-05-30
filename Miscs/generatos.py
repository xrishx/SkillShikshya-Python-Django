def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

# Using the generator
counter = count_up_to(100)
for number in counter:
    print(number)