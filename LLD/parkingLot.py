from enum import Enum
from abc import ABC
from datetime import datetime
import uuid


# =========================
# ENUMS
# =========================

class VehicleType(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3


class SpotType(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3


# =========================
# VEHICLE
# =========================

class Vehicle(ABC):
    def __init__(self, number: str, vehicle_type: VehicleType):
        self.number = number
        self.vehicle_type = vehicle_type


class Bike(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.BIKE)


class Car(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.TRUCK)


# =========================
# PARKING SPOT
# =========================

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def can_fit_vehicle(self, vehicle: Vehicle):
        return self.spot_type.value == vehicle.vehicle_type.value

    def park(self, vehicle: Vehicle):
        if not self.is_available():
            raise Exception("Spot already occupied")
        if not self.can_fit_vehicle(vehicle):
            raise Exception("Vehicle type mismatch")
        self.vehicle = vehicle

    def unpark(self):
        self.vehicle = None


# =========================
# PARKING FLOOR
# =========================

class ParkingFloor:
    def __init__(self, floor_number: int, spots: list):
        self.floor_number = floor_number
        self.spots = spots

    def find_available_spot(self, vehicle: Vehicle):
        for spot in self.spots:
            if spot.is_available() and spot.can_fit_vehicle(vehicle):
                return spot
        return None


# =========================
# TICKET
# =========================

class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()


# =========================
# PRICING STRATEGY
# =========================

class PricingStrategy:
    def calculate(self, ticket: Ticket):
        duration = datetime.now() - ticket.entry_time
        hours = max(1, int(duration.total_seconds() // 3600))

        if ticket.vehicle.vehicle_type == VehicleType.BIKE:
            return hours * 10
        elif ticket.vehicle.vehicle_type == VehicleType.CAR:
            return hours * 20
        else:
            return hours * 30


# =========================
# PARKING LOT
# =========================

class ParkingLot:
    def __init__(self, floors: list):
        self.floors = floors
        self.active_tickets = {}
        self.pricing_strategy = PricingStrategy()

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                spot.park(vehicle)
                ticket = Ticket(vehicle, spot)
                self.active_tickets[ticket.id] = ticket
                print(f"Vehicle parked at Spot {spot.spot_id} (Floor {floor.floor_number})")
                return ticket
        raise Exception("No available spot")

    def unpark_vehicle(self, ticket_id: str):
        if ticket_id not in self.active_tickets:
            raise Exception("Invalid Ticket")

        ticket = self.active_tickets[ticket_id]
        amount = self.pricing_strategy.calculate(ticket)

        ticket.spot.unpark()
        del self.active_tickets[ticket_id]

        print(f"Vehicle unparked from Spot {ticket.spot.spot_id}")
        print(f"Amount to pay: ₹{amount}")
        return amount


# =========================
# DEMO
# =========================

if __name__ == "__main__":
    # Create Spots
    floor1_spots = [
        ParkingSpot(1, SpotType.BIKE),
        ParkingSpot(2, SpotType.CAR),
        ParkingSpot(3, SpotType.TRUCK)
    ]

    floor1 = ParkingFloor(1, floor1_spots)

    # Create Parking Lot
    parking_lot = ParkingLot([floor1])

    # Park a Car
    car = Car("CG04AB1234")
    ticket = parking_lot.park_vehicle(car)

    # Unpark
    parking_lot.unpark_vehicle(ticket.id)
