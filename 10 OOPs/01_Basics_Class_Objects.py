#WAP TO CREATE A CLASS OF CAR

class Car:
    # __init__ : CONSTRUCTOR
    def __init__(self,user_brand,user_model): # TO PASS THE PARAMETERS

        # THESE ARE INSTANCES / ATTRIBUTES
        self.brand= user_brand
        self.model=user_model

# OBJECT 1
c1=Car("Toyota","Coralla") # ASSISGNED
print(c1.brand,c1.model) # ACCESSING

# OBJECT 2
c2=Car("Tata","Safari")
print(c2.brand,c2.model)



