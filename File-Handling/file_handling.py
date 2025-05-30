# syntax
# file = open("filename", "mode")

# Opening a file in read mode
file = open("File-Handling/example.txt", "r")
file.close()

# Opening a file in write mode
file = open("File-Handling/example.txt", "w")
file.close()

# Opening a file in append mode
file = open("File-Handling/example.txt", "a")
file.close()

# Opening a file in binary read mode
file = open("File-Handling/example.txt", "rb")
file.close()

# do not forget to close after open unless using 'with'
# write()
with open("File-Handling/example.txt", "w") as file:
    file.write("Hello, World!")
# writelines()
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("File-Handling/example.txt", "w") as file:
    file.writelines(lines)

# append mode
with open("File-Handling/example.txt", "a") as file:
    file.write("Appended line")

# read()
with open("File-Handling/example.txt", "r") as file:
    content = file.read()
    print(content)
# readline()
with open("File-Handling/example.txt", "r") as file:
    lines = file.readline()
    while lines:                    # using while
        print(lines, end='')
        lines = file.readline()
    lines = file.readlines()        # using for
    for line in lines:
        print(line, end='')


