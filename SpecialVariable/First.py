print("The name of the current module is:", __name__)
print("The file path is:", __file__)
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2,3))
def subtract(a, b):
    """Subtracts two numbers and returns the result."""
    return a - b

if __name__ == "__main__":
    print(subtract(5,3))

class A:
    pass
class B(A):
    pass
b=B
print(b.__base__)