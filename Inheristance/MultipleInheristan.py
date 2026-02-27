class Father:
    def skill1(self):
        print("Father's have Drinking skill")
class Mother:
    def skill2(self):
        print("Mother's have Cooking skill")
class Son(Father,Mother):
    def skill3(self):
        print("Son's have Playing skill")
s=Son()
s.skill1()
s.skill2()
s.skill3()