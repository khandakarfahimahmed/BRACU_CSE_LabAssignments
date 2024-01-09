class Student:
    Id = 0

    def __init__(self,name,department,age,cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa
        Student.Id +=1
    def get_details(self):
        print("ID:",Student.Id)
        print("Name:",self.name)
        print("Depertment:",self.department)
        print("Age:",self.age)
        print("CGPA:",self.cgpa)
    @classmethod
    def from_String(cls,a):
        name,department,age,cgpa = a.split("-")
        b = cls(name,department,age,cgpa)
        return b

#========================
s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()
#==========================

print("Class variables are usually variables that are shared by all instances but Instance variables are unique to each instance of the class and they are defined within a class method ")
print("Class methods do not need self as an argument but instance method need self as an argument")
