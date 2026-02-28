class Student:
    #default constructors
    def __init__(self):
        pass
    #parameterized constructores
    def __init__(self,name,marks,rollno):
        self.name=name
        self.marks=marks
        self.rollno=rollno
        print("adding new students in database")
 
s1 = Student("karan",66,1)
print(s1.name,s1.marks,s1.rollno)

s2 = Student("Arus",77,8)
print(s2.name,s2.marks,s2.rollno)

#Adding collage name in student detail
class Student:
    collage_name="IIT jhanjeri"
    #parameterized constructores
    def __init__(self,name,marks,rollno):
        self.name=name
        self.marks=marks
        self.rollno=rollno
        print("adding new students in database")
 
s1 = Student("karan",66,1)
print(s1.name,s1.marks,s1.rollno,s1.collage_name)

s2 = Student("Arus",77,8)
print(s2.name,s2.marks,s2.rollno,s2.collage_name)
