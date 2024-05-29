"""This module implements the Memento behavior pattern,
defining the VehicleMemento class

Author: Edison Alvarez - edisonalaverzv10@gmail.com
"""

from ..vehicles_subsystem import Vehicle

class VehicleMemento():
    """
    This class is responsible for saving a state or
    instance of the vehicle class
    """
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def get_vehicle(self):
        """
        This method returns the saved object,
        it does not receive parameters
        """
        return self.vehicle
