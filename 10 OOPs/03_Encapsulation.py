# MODIFY THE CAR CLASS TO ENCAPSULATE THE BRAND ATTRIBUTE 
# MAKING IT PRIVATE AND PROVIDE A GETTER MEHTOD TO IT

class Car():
    def __init__(self,brand,model):
        self.__brand = brand # __ private ho jyga
        self.model = model

    def get_brand(self):
        return self.__brand

#ELECTRIC CAR INHERITED CLASS CAR IN ITSELF COMPLETELY
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) # ALREADY TAKE SELF FROM UPPER CLASS
        self.battery = battery_size

my_Car=ElectricCar("Tesla","Model S","100kWh")
print(my_Car.get_brand())