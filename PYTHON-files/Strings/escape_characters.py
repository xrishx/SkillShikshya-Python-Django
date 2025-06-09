# followed by \
# normal string interprets escape character unless it's a raw character

# \n prints newline
normal = "Hello\nWorld"
raw = r"Hello\nWorld"

print(normal)       # Prints the newline
print(raw)          # Prints \n as it is

# \\ for backslash
# \' to print '
# \" to print "