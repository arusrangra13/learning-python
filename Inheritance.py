class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopprd.")


class Maruticar(Car):
    def __init__(self,name):
        self.name = name

car1 = Maruticar("Alto")
car2  = Maruticar("Dizre")

print(car1.start())

       
