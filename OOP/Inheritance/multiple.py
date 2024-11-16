class Vehicle:
    def __init__(self,wheels,fuel_type) :
        self.wheels = wheels
        self.fuel_type = fuel_type

    def display_vehicle_info_(self):
        print(f"Vehicle info \n  wheels : {self.wheels} , fuel type : {self.fuel_type}")

class electric:
    def __init__(self,battery_capacity,charging_time):
        self.battery_capacity = battery_capacity
        self.charging_time = charging_time

    def display_Electric_info_(self):
             print(f"Electric info \n Battery capacity : {self.battery_capacity} , Charging time : {self.charging_time}")

class ElectricCar(electric,Vehicle):
     def __init__(self, wheels,fuel_type,battery_capacity, charging_time,brand):
          super().__init__(self,battery_capacity, charging_time)
          super().__init__(self,wheels,fuel_type)
          self.brand = brand

     def display_ElectricCar_info_(self):
          super().display_ElectricCar_info_()
          super().display_vehicle_info_()
          print(f"Car Brand : {self.brand}")       

          