# Updating car speed
class Car:   
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def update_speed(self, speed):
        self.speed = speed

    def show(self):
        print(self.brand, self.speed)

c1 = Car("BMW", 200)
c1.show()

c1.update_speed(250)
c1.show()
