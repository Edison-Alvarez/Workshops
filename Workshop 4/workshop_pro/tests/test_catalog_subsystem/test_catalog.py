"""
This is a file to test the CatalogConcrete class of the Catalogs subsystem.

Author: Author: Edison Alvarez - edisonalaverzv10@gmail.com
"""

from workshop_pro.catalog_subsystem.catalog import CatalogConcrete

class TestCatalogConcrete:
    """This class contains the tests for the CatalogConcrete class of the Catalogs subsystem."""

    @classmethod
    def setup_class(cls):
        """
        This method is executed before each test method.
        """
        cls.catalog = CatalogConcrete()
        cls.vehicle_data = {
            "type": "car",
            "speed": 150,
            "price": 20000,
            "brand": "Toyota"
        }

    def test_add_vehicle(self):
        """
        This method is a unit test for the add_vehicle method of the CatalogConcrete class.
        """
        self.catalog.add_vehicle(self.vehicle_data["type"])
        all_vehicles = self.catalog.get_all_vehicles()
        assert len(all_vehicles) == 1
        assert all_vehicles[1].type == self.vehicle_data["type"]

    def test_get_all_vehicles(self):
        """
        This method is a unit test for the get_all_vehicles method of the CatalogConcrete class.
        """
        self.catalog.add_vehicle(self.vehicle_data["type"])
        all_vehicles = self.catalog.get_all_vehicles()
        assert len(all_vehicles) == 1

    def test_get_by_speed(self):
        """
        This method is a unit test for the get_by_speed method of the CatalogConcrete class.
        """
        min_speed = 100
        max_speed = 200
        self.catalog.add_vehicle(self.vehicle_data["type"])
        vehicles_in_speed_range = self.catalog.get_by_speed(min_speed, max_speed)
        assert len(vehicles_in_speed_range) == 1

    def test_get_by_price(self):
        """
        This method is a unit test for the get_by_price method of the CatalogConcrete class.
        """
        min_price = 15000
        max_price = 25000
        self.catalog.add_vehicle(self.vehicle_data["type"])
        vehicles_in_price_range = self.catalog.get_by_price(min_price, max_price)
        assert len(vehicles_in_price_range) == 1

    def test_remove_vehicle(self):
        """
        This method is a unit test for the remove_vehicle method of the CatalogConcrete class.
        """
        self.catalog.add_vehicle(self.vehicle_data["type"])
        vehicle = self.catalog.get_all_vehicles()[0]
        self.catalog.remove_vehicle(vehicle)
        all_vehicles = self.catalog.get_all_vehicles()
        assert len(all_vehicles) == 0

    def test_save_memento(self):
        """
        This method is a unit test for the save_memento method of the CatalogConcrete class.
        """
        self.catalog.add_vehicle(self.vehicle_data["type"])
        vehicle = self.catalog.get_all_vehicles()[0]
        memento = self.catalog.save_memento(vehicle)
        assert memento.get_vehicle() == vehicle

    def test_restore_vehicle(self):
        """
        This method is a unit test for the restore_vehicle method of the CatalogConcrete class.
        """
        self.catalog.add_vehicle(self.vehicle_data["type"])
        vehicle = self.catalog.get_all_vehicles()[0]
        memento = self.catalog.save_memento(vehicle)
        self.catalog.remove_vehicle(vehicle)
        self.catalog.restore_vehicle(memento)
        all_vehicles = self.catalog.get_all_vehicles()
        assert len(all_vehicles) == 1
        assert all_vehicles[0] == vehicle
