import time

start_time2 = time.time()

for i in range(0, 10):
    while i % 2 == 0:
        print(f"Even numbers are: {i}")
        break

end_time2 = time.time()

execution_time2 = end_time2 - start_time2
print(f"Execution time in While inside For Loop: {execution_time2}")