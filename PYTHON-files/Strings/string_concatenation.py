# Joining two or more strings together

w1 = "Hello"
w2 = "World"

# using + operator
w3 = w1+w2
print(w3)   # HelloWorld

# with space
blank = " "
w3 = w1+blank+w2 # or w1 + " " + w2
print(w3)

# using * operator
w3 = w1 * 3 # HelloHelloHello
print(w3)

# can use + * together
w3 = w1 + w2 * 2    # HelloWorldWorld
print(w3)
