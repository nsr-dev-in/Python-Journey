# FUEL DAL DO

class Car():
    def __init__(self,brand,model):
        self.__brand = brand # __ private ho jyga
        self.model = model

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self): # POLYMORPHISM
        return "Petrol or Disel"

#ELECTRIC CAR INHERITED CLASS CAR IN ITSELF COMPLETELY
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) # ALREADY TAKE SELF FROM UPPER CLASS
        self.battery = battery_size
    
    def fuel_type(self): # POLYMORPHISM
        return "Electric Charge"

MEC=ElectricCar("Tesla","Model S","100kWh")
MC=Car("Tata","Safari")

print(MC.fuel_type())
print(MEC.fuel_type())