"""
This module contains the Facade class that provides a simple interface 
to the complex logic of the Engines subsystem.

Authors: Carlos Sierra - cavirguez@udistrital.edu.co / Edison Alvarez - edisonalaverzv10@gmail.com
Update: Edison Alvarez - edisonalaverzv10@gmail.com (28/05/2024)
"""

from .factories import HighEngineFactory, LowEngineFactory
from .engines import Engine

# pylint: disable=too-few-public-methods
class EnginesFacade:
    """
    This class is a Facade Pattern Design that provides a
    simple interface to the complex logic of the Engines subsystem.

    Methods:
        get_engine -> Engine: This method returns an engine object based on the type and price.
    """

    high_factory = HighEngineFactory()
    low_factory = LowEngineFactory()

    @staticmethod
    def get_engine(type_engine: str, price_engine: str) -> Engine:
        """
        This method returns an engine object based on the type and price.

        Args:
            type_engine (str): The type of the engine.
            price_engine (str): The price of the engine.

        Returns:
            An engine based on parameters.
        """

        factories = {
            "high": EnginesFacade.high_factory,
            "low": EnginesFacade.low_factory,
        }

        engine_creators = {
            "electric": lambda factory: factory.create_electric_engine(),
            "gas": lambda factory: factory.create_gas_engine(),
            "hybrid": lambda factory: factory.create_hybrid_engine(),
        }

        if price_engine not in factories:
            raise ValueError("Invalid price value")

        if type_engine not in engine_creators:
            raise ValueError("Invalid engine type")

        factory = factories[price_engine]
        engine = engine_creators[type_engine](factory)

        return engine
