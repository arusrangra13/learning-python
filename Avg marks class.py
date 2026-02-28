class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is:",sum/3)

s1= student("Rahul",[56,76,88])
s2= student("Raju",[78,79,90])
s3= student("Anjali",[90,87,65])

s1.get_avg()
s2.get_avg()
s3.get_avg()
