x=100
def display():

    x=200
    def inner():
        nonlocal x#nonlocal variable can be used inside the inner function by using nonlocal keyword
        x=300
        print(x)
    inner()
    print(x)
display()
print(x)