marks = 50 # global variable
def myf():
    marks = 70 # local variable
    print(marks) # prints local value

myf()
print(marks) #print global value
