"""
This is a file to test the performance decorators of the Catalogs subsystem.

Author: Carlos Sierra <cavirguezs@udistrital.edu.co>
"""

import time
from workshop_pro.workshop_pro.catalog_subsystem.decorator import (
    TimePerformanceDecorator
)
from workshop_pro.workshop_pro.catalog_subsystem.catalog import CatalogConcrete
from workshop_pro.workshop_pro.observability_subsystem.observability import (
    Observability,
)
from workshop_pro.engines_subsystem.engines import Engine


class TestTimePerformanceDecorator:
    """This class tests the TimePerformanceDecorator class"""

    @classmethod
    def setup_class(cls):
        """This is a method to create dummy data for catalog"""
        cls.catalog = CatalogConcrete()
        cls.decorated_catalog = TimePerformanceDecorator(cls.catalog)

    def test_get_all_vehicles(self):
        """This is a test case to verify the time performance of getting all vehicles"""
        start = time.time()
        self.decorated_catalog.get_all_vehicles()
        end = time.time()
        Observability.write_performance_log.assert_called_with(
            f"get_all_vehicles took {end - start} seconds"
        )

    def test_get_by_speed(self):
        """This is a test case to verify the time performance of getting vehicles by speed"""
        start = time.time()
        self.decorated_catalog.get_by_speed(100, 200)
        end = time.time()
        Observability.write_performance_log.assert_called_with(
            f"get_by_speed took {end - start} seconds"
        )

    def test_get_by_price(self):
        """This is a test case to verify the time performance of getting vehicles by price"""
        start = time.time()
        self.decorated_catalog.get_by_price(15000, 25000)
        end = time.time()
        Observability.write_performance_log.assert_called_with(
            f"get_by_price took {end - start} seconds"
        )

    def test_add_vehicle(self):
        """This is a test case to verify the time performance of adding a vehicle"""
        start = time.time()
        self.decorated_catalog.add_vehicle("car")
        end = time.time()
        Observability.write_performance_log.assert_called_with(
            f"add_vehicle took {end - start} seconds"
        )

    def test_remove_vehicle(self):
        """This is a test case to verify the time performance of removing a vehicle"""
        vehicle = self.catalog.get_all_vehicles()[0]
        start = time.time()
        self.decorated_catalog.remove_vehicle(vehicle)
        end = time.time()
        Observability.write_performance_log.assert_called_with(
            f"remove_vehicle took {end - start} seconds"
        )
