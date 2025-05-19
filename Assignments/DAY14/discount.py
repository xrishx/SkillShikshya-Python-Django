discount = 0
amount = int(input("Enter an amount: "))

if amount >= 1000:
    discount = amount * 10/100
elif 1000 > amount >= 500:
    discount = amount * 5/100
elif 500 > amount >= 200:
    discount = amount * 2/100
else:
    discount = 0

print("Amount = ", amount - discount)