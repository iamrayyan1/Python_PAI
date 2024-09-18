# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any
# vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on
# full fare as a maintenance charge. So total fare for bus instance will become the final amount =
# total fare + 10% of the total fare. [2 marks]

class Vehicle:
    def __init__(self,seating_capacity):
      self.seating_capacity = seating_capacity

    def fare(self):
      return self.seating_capacity*100
  
class Bus(Vehicle):
  def fare(self):
    total_fare = super().fare()
    new_fare = total_fare + (total_fare*0.10)
    return new_fare

v = Vehicle(10)
print(f"Vehicle fare is: {v.fare()}")
b = Bus(50)
print(f"bus fare is: {b.fare()}")
