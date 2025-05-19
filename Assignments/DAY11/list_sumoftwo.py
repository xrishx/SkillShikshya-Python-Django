lst = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
list_length = len(lst)

# Function to check if there exists a pair in the list whose sum is equal to the given value 'k'
def check_sum(lst, k):   
    # Loop through each element in the list
    for i in range(list_length):
        # Nested loop to compare each element with subsequent elements
        for j in range(i+1, list_length):
            # Check if the sum of the current pair is equal to 'k'
            if lst[i] + lst[j] == k:
                return "Exists"  # Return True if such a pair is found
    return "Doesn't Exist"  # Return False if no such pair is found


x = 0
while x < list_length:
    k = lst[x]
    check_sum(lst, k)
    x += 1


