class stu:
    def __init__(self,name,rollno,section):
        self.name=name
        self._rollno=rollno
        self.__section=section
    def show(self):
        print("Name:",self.name)
        print("Roll No:",self._rollno)
        print("Section:",self.__section)
class info(stu):
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self._rollno)
        print("Section:",self.__section)
s=stu("Kiran",101,"A")
s.show()
Info1=info("Kiran",101,"A")
Info1.display()