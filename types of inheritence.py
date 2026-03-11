#Single inheritence
class car:

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped.")


class MarutiCar(car):
    def __init__(self, name):
        self.name = name


car1 = MarutiCar("Alto")
car2 = MarutiCar("Swift")

car1.start()
car2.stop()

#Multi level inhertence
class car:
    
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped.")

class MarutiCar(car):
    def __init__(self,Brand):
        self.Brand = Brand

class Swift(MarutiCar):
    def __init__(self,type):
        self.type = type
    
car1 = Swift("petrol")
car1.start()
