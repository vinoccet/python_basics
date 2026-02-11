class Vehicle:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    def start(self):
        print("start a vehicle")

class Car(Vehicle):

    def start(self):
        print("start a car") 

class MotorBike(Vehicle):
     
    def start(self):
        print("Bike started")    

vehicles=[Car("Hoda","Honda City"),MotorBike("Yamaha","FZ")]   

# for vehicle in vehicles:
#     if isinstance(vehicle,Car):
#         vehicle.start()
#     elif isinstance(vehicle,MotorBike): 
#         vehicle.start_bike()

for vehicle in vehicles:
    vehicle.start()