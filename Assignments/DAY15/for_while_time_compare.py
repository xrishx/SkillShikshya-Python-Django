import time
start_time1 = time.time()

i = 0
while i < 10:
    for j in range(i, i+1):
        if j % 2 == 0:
            print(f"Even numbers are: {j}")
    i += 1

end_time1 = time.time()

execution_time1 = end_time1 - start_time1
print(f"Execution time in For inside While Loop: {execution_time1}")

start_time2 = time.time()

for i in range(0, 10):
    while i % 2 == 0:
        print(f"Even numbers are: {i}")
        break

end_time2 = time.time()

execution_time2 = end_time2 - start_time2
print(f"Execution time in While inside For Loop: {execution_time2}")

print(f"Difference in execution time between them is:")
if execution_time1 > execution_time2:
    print("For inside While Loop is faster by", execution_time1 - execution_time2)
elif execution_time2 > execution_time1:
    print("For inside While Loop is faster by", execution_time2 - execution_time1)