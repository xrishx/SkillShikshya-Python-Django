# String Indexing
# POSITIVE indexing starts at 0

var = "Hello Python"

print(var[0])   # H
print(var[7])   # Y
print(var[11])  # N
print(var[12])  # ERROR!

# NEGATIVE indexing starts at -1

print(var[-1])  # N
print(var[-5])  # Y
print(var[-12]) # H

# String Slicing using :
print(var[3:8]) # lo Py

# Slicing with Negative indexing
print(var[-9:-4])   # lo Py

# Note:
print(var[0:5])     # Hello
print(var[:5])      # Hello
#similarly
print(var[6:12])    # Python
print(var[6:])      # Python
# also
# left operand must be smaller than right operand

# Multiple Slicing
print(var[:6][:2])  # HE
# slicing :6 then does :2 to the result