#WAP TO CREATE AN ELECTRIC CAR CLASS THAT INHERITS FROM THE CAR CLASS AND HAS AN ADDITIONAL ATTRIBUTE BATTERY_SIZE

class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

#ELECTRIC CAR INHERITED CLASS CAR IN ITSELF COMPLETELY
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) # ALREADY TAKE SELF FROM UPPER CLASS
        self.battery = battery_size

my_Car=ElectricCar("Tesla","Model S","100kWh")
print(my_Car.brand,my_Car.model,my_Car.battery)