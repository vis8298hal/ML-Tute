class Vehicle:
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("car")
        self.enginetype = enginetype
        self.wheels = 4
        self.doors = 4
    def drive(self, speed):
        super().drive(speed)
        print(f"Driving Car of Engine Type {self.enginetype} at speed {self.speed}")

class Motorcycle(Vehicle):
    def __init__(self, enginetype, sidecar=False):
        super().__init__("motorcycle")
        self.enginetype = enginetype
        self.sidecar = sidecar
        if sidecar:
            self.wheels = 3
        else:
            self.wheels = 2

        self.doors = 0
    def drive(self, speed):
        super().drive(speed)
        print(f"Driving Motorcycle of Engine Type {self.enginetype} at speed {self.speed}")

if __name__ == "__main__":
    car1 = Car("gas")
    car2 = Car("electric")
    bike1 = Motorcycle("d12", False)
    bike2 = Motorcycle("v8", True)

    print(car1.doors, car1.enginetype, car1.bodystyle, car1.wheels)

    print(car2.doors, car2.enginetype, car2.bodystyle, car2.wheels)
    print(bike1.sidecar, bike1.enginetype, bike1.bodystyle, bike1.wheels)
    print(bike2.sidecar, bike2.enginetype, bike2.bodystyle, bike2.wheels)

    car1.drive(60)
    car2.drive(120)
    bike1.drive(40)
    bike2.drive(50)
