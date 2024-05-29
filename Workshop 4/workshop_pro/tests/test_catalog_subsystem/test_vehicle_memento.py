""" 
This is a file to test the VehicleMemento class of the Catalogs subsystem. 
Author: Author: Edson Alvarez - edisonalaverzv10@gmail.com 
"""

import pytest
from workshop_pro.vehicles_subsystem.vehicle import Vehicle
from workshop_pro.catalog_subsystem.vehicle_memento import VehicleMemento
from workshop_pro.engines_subsystem.engines import Engine


class TestVehicleMemento:
    """This class tests the VehicleMemento class"""

    @pytest.fixture
    def vehicle(self):
        """Fixture to create a dummy vehicle instance"""
        engine = Engine(
            100,
            200,
            "100x100x100",
            150,
            "medium",
            100.5,
        )
        return Vehicle(
            chassis="123ABC", price=20000.0, engine=engine, model="Corolla", year=2020
        )

    @pytest.fixture
    def vehicle_memento(self, vehicle):
        """Fixture to create a VehicleMemento instance"""
        return VehicleMemento(vehicle)

    def test_vehicle_memento_initialization(self, vehicle, vehicle_memento):
        """Test the initialization of VehicleMemento"""
        assert vehicle_memento.vehicle == vehicle

    def test_get_vehicle(self, vehicle, vehicle_memento):
        """Test the get_vehicle method"""
        assert vehicle_memento.get_vehicle() == vehicle
