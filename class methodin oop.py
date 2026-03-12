class Person:
    name = "Arus rangra"
    @classmethod
    def changeName(cls,name):
        cls.name =name

p1 = Person()
p1.changeName("Ram")
print(p1.name)
print(Person.name)
