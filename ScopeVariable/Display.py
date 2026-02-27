#x=100#global variable
def display():
    global x#global variable can be used inside the function by using global keyword
    x=10   #local variable  
    print(x)
display()
print(x)