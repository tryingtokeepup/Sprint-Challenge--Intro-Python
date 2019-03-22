# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    def __init__(self):
        # this is the base class, Vehicle, which will be the base for all other classes.
        pass


class FlightVehicle(Vehicle):
    def __init__(self):
        # this will be the base class for Starship and Airplane
        pass

# Flight Vehicle classes and children


class Starship(FlightVehicle):
    def __init__(self):
        # this will inherit from FlightVehicle
        pass


class Airplane(FlightVehicle):
    def __init__(self):
        # this will also inherit from FlightVehicle
        pass

# Ground Vehicle classes and children


class GroundVehicle(Vehicle):
    def __init__(self):
        # this will serve as the base class for the other ground vehicles, and inherits from Vehicle
        pass


class Car(GroundVehicle):
    def __init__(self):
        # inherits from GroundVehicle
        pass


class Motocycle(GroundVehicle):
    def __init__(self):
        # inherits from GroundVehicle
        pass
