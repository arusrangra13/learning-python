class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=False
        self.brk=True
        self.clutch=True
        print("car started..")

car1=car()
car1.start()

car2=car()
car2.start()
