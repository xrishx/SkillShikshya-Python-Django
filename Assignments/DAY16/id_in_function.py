def testfunction(arg):
    print("ID inside the function", id(arg))
    arg += 1
    print("new object after increment", arg, id(arg))

var = 10
print("ID before passing: ", id(var))
testfunction(var)
print("Value after function call", var)

