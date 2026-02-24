# basic code 
class Student:
    name = "ram"

s1 = Student()
print(s1.name)

# using function 
class Student:
    def __init__(self,fullname):
        self.name=fullname
 
s1 = Student("karan")
print(s1.name)
