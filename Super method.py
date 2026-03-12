class car:
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped.")

class MarutiCar(car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

car1 = MarutiCar("Alto","Petrol")
print(car1.type)
