# String are sequence type like list
# Can use insert() append() remove()

s1 = 'word'
print("Original String: ", s1)
l1 = list(s1)

l1.insert(3, 'l')
# adding 'l' on 3 index

print(l1)

s1 = "".join(l1)
print("Modified string: ", s1)

