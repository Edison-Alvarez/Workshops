"""
This module has a definition of both an interface and a concrete definition for Catalogs.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

from typing import List

from .catalog_interface import Catalog
from ..vehicles_subsystem import Vehicle, VehiclesFacade
from .vehicle_memento import VehicleMemento

class CatalogConcrete(Catalog):
    """
    This is a concrete implementation of the Catalog interface.

    Methods:
        get_all_vehicles -> list: This method returns a list of all vehicles in the catalog.
        get_by_speed -> List[Vehicle]: This method returns a list of vehicles that have a speed
                                       between min_speed and max_speed.
        get_by_price -> List[Vehicle]: This method returns a list of vehicles that have a price
                                       between min_price and max_price.
        add_vehicle: This method adds a vehicle to the catalog.
        remove_vehicle: This method removes a vehicle from the catalog.
    """

    def __init__(self):
        self.__vehicles = []
        self.__vehicles_facade = VehiclesFacade()

    def get_all_vehicles(self) -> List[Vehicle]:
        """
        Returns a list of all vehicles in the catalog.

        Returns:
            List[Vehicle]: The list of all vehicles.
        """
        return self.__vehicles

    def get_by_speed(self, min_speed: int, max_speed: int) -> List[Vehicle]:
        """
        Returns a list of vehicles that have a speed within the specified range.

        Args:
            min_speed (int): The minimum speed of the vehicles to retrieve.
            max_speed (int): The maximum speed of the vehicles to retrieve.

        Returns:
            List[Vehicle]: A list of vehicles within the specified speed range.
        """
        return [
            vehicle
            for vehicle in self.__vehicles
            if vehicle.is_in_speed(min_speed, max_speed)
        ]

    def get_by_price(self, min_price: int, max_price: int) -> List[Vehicle]:
        """
        Returns a list of vehicles that have a price within the specified range.

        Args:
            min_price (float): The minimum price of the vehicles to retrieve.
            max_price (float): The maximum price of the vehicles to retrieve.

        Returns:
            List[Vehicle]: A list of vehicles within the specified price range.
        """
        return [
            vehicle
            for vehicle in self.__vehicles
            if vehicle.is_in_price(min_price, max_price)
        ]

    def add_vehicle(self, vehicle_type: str):
        """
        Adds a new vehicle of the specified type to the catalog.

        Args:
            vehicle_type (str): The type of the vehicle to add.
        """
        self.__vehicles.append(self.__vehicles_facade.create_vehicle(vehicle_type))

    def remove_vehicle(self, vehicle: Vehicle):
        """
        Removes the specified vehicle from the catalog.

        Args:
            vehicle (Vehicle): The vehicle to remove.
        """
        self.save_memento(vehicle)
        self.__vehicles.remove(vehicle)

    def save_memento(self, vehicle: Vehicle):
        """
        This method saves a vehicle object, creating a 
        vehicle_memento object.
        
        Args:
            vehicle (Vehicle): The vehicle to save.
        """
        memento = VehicleMemento(vehicle)
        return memento

    def restore_vehicle(self, memento: VehicleMemento):
        """
        This method restores a vehicle object to the catalog
        
        Args:
            memento (VehicleMemento): The VehicleMemento that
            contains the vehicle to be restored
        """
        vehicle = memento.get_vehicle()
        self.__vehicles.append(vehicle)
        print("The last vehicle was correctly restored.")
