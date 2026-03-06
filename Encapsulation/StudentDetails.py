class stu:
    def __init__(self,name,rollno,section,marks):
        self.name=name
        self._rollno=rollno
        self.section=section
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        self.__marks=marks
class info(stu):
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self._rollno)
        print("Section:",self.section)
        print("Marks:",self.get_marks())
s=stu("Kiran",101,"A",85)
print("Marks:",s.get_marks())
s.set_marks(90)
print("Marks:",s.get_marks())
