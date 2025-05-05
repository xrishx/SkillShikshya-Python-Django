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

var1 = 50
var2 = 60 
def myfunction():
    #Change values of Global Variable
    globals()['var1'] = globals()['var1'] + 10
    global var2
    var2 = var2 + 20

myfunction()
print(f"Var1: {var1}")
print(f"Var2: {var2}")


