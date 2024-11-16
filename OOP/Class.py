
class car :
        def __init__(self,company,model,year,distance):
                self.company = company
                self.model = model
                self.year = year
                self.distance = distance

        def carInfo(self):
                return f"{self.company} {self.model} {self.year}"

        def status(self):
                return f"{self.model} is currently in running condition"

        def traveled(self):
                return f"{self.model} is traveled {self.distance}K.M"       
        

new_car = car("Toyota" , "fortuner" , 2016 , 5000)

print(new_car)
print(new_car.carInfo())
print(new_car.status())
print(new_car.traveled())