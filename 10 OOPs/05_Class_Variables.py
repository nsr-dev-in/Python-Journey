# COUNT NO. OF CARS CREATED

class Car():
    total_cars=0 # counter 
    def __init__(self,brand,model):
        self.__brand = brand # __ private ho jyga
        self.model = model

        Car.total_cars += 1

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
MEC1=ElectricCar("Tesla","Model S","100kWh")
MEC2=ElectricCar("Tesla","Model S","100kWh")

MC=Car("Tata","Safari")
MC1=Car("Tata","Safari")
MC2=Car("Tata","Safari")

print(Car.total_cars) #PRINT TOTAL NO .OF CARS CREATED