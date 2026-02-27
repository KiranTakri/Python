x="Global"
def outer():
    x="Outer"
    def inner():
        nonlocal x #nonlocal variable can be used inside the inner function by using nonlocal keyword
        x="Inner"
        print(x)
    inner()
    print(x)
outer()
print(x)

