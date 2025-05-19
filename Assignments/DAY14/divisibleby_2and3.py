num = int(input("Enter your number: "))
print("Your number is: ", num)

if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by 2 and 3.")
else:
    print("No Divisible by 2 and 3.")


print("-------Execution Ends-------")