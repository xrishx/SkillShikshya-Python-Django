# Given n integer, array values and an inter k, find the min and max median overall of subsequence of length k


n = int(input("Enter the number of integers: "))

values = []
for i in range(1, n+1):
    values.append(i)
    
print(values)
print(n)

k = int(input("Enter the length of subsequences: "))

subsequences = []

for i in range(n):
    for j in range(i + 1, n):
        subsequences.append([values[i], values[j]])

median  = int((k + 1) / 2)
median = median - 1     # index starts at 0
median_list = []

for sub in subsequences:
    median_list.append(sub[median])

min_median = min(median_list)
max_median = max(median_list)

print(f"Max Median is: {max_median}")
print(f"Min Median is: {min_median}")