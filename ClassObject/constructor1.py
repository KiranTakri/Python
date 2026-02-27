class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)
s=student("Rajendra",69)
s1=student("Rashmi",19)
s.display()
s1.display()
