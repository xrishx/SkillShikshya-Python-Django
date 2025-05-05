name = "TT"
marks = 50
result = True
def myf():
    a = 10
    b = 20
    c = a + b
    print(f"Locals: {locals()}")
    print(f"Globals: {globals()}")
    return c

myf()


