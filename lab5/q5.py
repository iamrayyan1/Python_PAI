# You are tasked with developing a software system to manage vehicle rentals for a car rental
# company. The company offers different types of vehicles for rent, including cars, SUVs, and trucks. Each vehicle has attributes like the make, model, rental price, and availability status.
#  Design a class hierarchy to represent different types of vehicles (e.g., Car, SUV,
# Truck).
#  Implement methods within each vehicle class to check availability, calculate the total
# rental cost for a given period, and display vehicle details. Ensure that the availability
# status changes when a vehicle is rented or returned.
#  Create a class for managing rental reservations (e.g., RentalReservation) that connects a
# customer to a rented vehicle. This class should include details like the rental start date,
# end date, and the customer renting the vehicle.
#  Design a customer class (e.g., Customer) to store information about renters, including
# name, contact information, and rented vehicles. Implement a method to display a
# customer's rental history.
#  Demonstrate polymorphism by creating a function or method that can display the
# details of any vehicle (Car, SUV, Truck) or rental reservation (RentalReservation).
 
#  Incorporate encapsulation principles to protect sensitive information like rental prices and customer contact details. 

from datetime import datetime

class Vehicle:
    def __init__(self, make, model, rental_rate):
        self.make = make
        self.model = model
        self._rental_rate = rental_rate  
        self.availability = True
    
    def total_rental_cost(self, start_date, end_date):
        days = (end_date - start_date).days
        rental_cost = self._rental_rate * days
        return rental_cost
    
    def availability_status(self):
        if self.availability:
            print(f"The {self.make} {self.model} is available")
        else:
            print(f"The {self.make} {self.model} is not available")
    
    def display(self):
        print(f"Make: {self.make}\nModel: {self.model}\nRental Rate: {self._rental_rate}\nAvailability: {self.availability}")

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            print(f"The {self.make} {self.model} has been rented.")
        else:
            print(f"Sorry, the {self.make} {self.model} is already rented.")

    def return_vehicle(self):
        self.availability = True
        print(f"The {self.make} {self.model} has been returned and is now available.")


class Car(Vehicle):
    def __init__(self, make, model, rental_rate):
        super().__init__(make, model, rental_rate)
        self.type = "Car"

    def display(self):
        print("Vehicle Type: Car")
        super().display()


class SUV(Vehicle):
    def __init__(self, make, model, rental_rate):
        super().__init__(make, model, rental_rate)
        self.type = "SUV"

    def display(self):
        print("Vehicle Type: SUV")
        super().display()


class Truck(Vehicle):
    def __init__(self, make, model, rental_rate):
        super().__init__(make, model, rental_rate)
        self.type = "Truck"

    def display(self):
        print("Vehicle Type: Truck")
        super().display()


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.total_cost = vehicle.total_rental_cost(self.start_date, self.end_date)
    
    def display(self):
        print(f"Rental Reservation for {self.customer.name}:")
        print(f"Vehicle: {self.vehicle.make} {self.vehicle.model}")
        print(f"Start Date: {self.start_date.date()}")
        print(f"End Date: {self.end_date.date()}")
        print(f"Total Cost: ${self.total_cost:.2f}")
        print(f"Vehicle Availability: {self.vehicle.availability}")


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self._contact_info = contact_info 
        self.rental_history = []

    def add_rental(self, reservation):
        self.rental_history.append(reservation)

    def display_rental_history(self):
        if self.rental_history:
            print(f"{self.name}'s Rental History:")
            for reservation in self.rental_history:
                reservation.display()
        else:
            print(f"{self.name} has no rental history.")

    def display_contact_info(self):
        print(f"Customer Contact Info: {self._contact_info}")


def display_vehicle_details(vehicle):
    vehicle.display()

def display_reservation_details(reservation):
    reservation.display()


car1 = Car("Toyota", "Corolla", 50)
suv1 = SUV("Ford", "suv", 75)
truck1 = Truck("hyundai", "1500", 100)

display_vehicle_details(car1)
display_vehicle_details(suv1)
display_vehicle_details(truck1)

customer1 = Customer("Rija Ali", "rija@fast.com")
reservation1 = RentalReservation(customer1, car1, "2023-09-1", "2023-09-15")

display_reservation_details(reservation1)

customer1.add_rental(reservation1)
customer1.display_rental_history()

car1.rent_vehicle()
car1.return_vehicle()
