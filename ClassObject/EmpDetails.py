class Employe:
    def __init__(self,name,id,designation):
        self.name=name
        self.id=id
        self.designation=designation
    def emp(self):
        print("Name of Employe is : ",self.name)
        print("Age of Employe is : ",self.id)
        print("Designation of Employe is : ",self.designation)
e1=Employe("Raghav",1,"Engineer")
e1.emp()
print(e1.name)
#Assigning value to object
e1.name="Chadda"
#Adding new variable to the existing class
e1.city="Gunupur"
print(e1.city)
#deleting object
del e1.name
print(e1.name)

        