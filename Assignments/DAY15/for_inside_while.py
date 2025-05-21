import time
start_time = time.time()

i = 0
while i < 100:
    for j in range(i, i+1):
        if j % 2 == 0:
            print(f"Even numbers are: {j}")
    i += 1

end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time is {execution_time}")