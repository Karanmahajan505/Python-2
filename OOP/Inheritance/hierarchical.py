class Vehicle:
    def __init__(self,wheels,fuel_type) :
        self.wheels = wheels
        self.fuel_type = fuel_type

    def display_vehicle_info_(self):
        print(f"Vehicle info \n  wheels : {self.wheels} , fuel type : {self.fuel_type}")
 
        