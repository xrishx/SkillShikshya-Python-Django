rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == 0:
            print("*", end="")
        elif (i == 0 or i == 3) and j < cols - 1: 
            print("*", end="")
        elif j == cols - 1 and i > 0 and i < 3:  
            print("*", end="")
        elif i - j == 3: 
            print("*", end="")
        else:
            print(" ", end="")
    print()