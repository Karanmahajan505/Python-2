# Grandparent Class
class Vehicle:
    def __init__(self, wheels, fuel_type, speed):
        self.wheels = wheels
        self.fuel_type = fuel_type
        self.speed = speed

    def display_vehicle_info_(self):
        print(f"Vehicle info \nWheels: {self.wheels}, Fuel Type: {self.fuel_type}, Speed: {self.speed} km/h")

# Parent Class
class Car(Vehicle):
    def __init__(self, wheels, fuel_type, speed, doors, transmission, engine_type):
        super().__init__(wheels, fuel_type, speed)
        self.doors = doors
        self.transmission = transmission
        self.engine_type = engine_type

    def display_car_info_(self):
        super().display_vehicle_info_()
        print(f"Car info \nDoors: {self.doors}, Transmission: {self.transmission}, Engine Type: {self.engine_type}")

# Child Class
class ElectricCar(Car):
    def __init__(self, wheels, fuel_type, speed, doors, transmission, engine_type, battery_capacity, charging_time):
        super().__init__(wheels, fuel_type, speed, doors, transmission, engine_type)
        self.battery_capacity = battery_capacity
        self.charging_time = charging_time

    def display_ElectricCar_info_(self):
        super().display_car_info_()
        print(f"Electric Car Info \nBattery Capacity: {self.battery_capacity} kWh, Charging Time: {self.charging_time} hours")

electric_car = ElectricCar(4, "Electricity", 100, 4, "Auto", "Electric Motor", 75, 1.3)

electric_car.display_ElectricCar_info_()
