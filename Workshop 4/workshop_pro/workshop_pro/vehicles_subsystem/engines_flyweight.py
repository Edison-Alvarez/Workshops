"""
This files contains the Flyweight implementation for the Engines Sub-system.
The idea is to reutilize the common engines across the vehicles.

Authors: Carlos Sierra - cavirguez@udistrital.edu.co / Edison Alvarez - edisonalaverzv10@gmail.com
Update: Edison Alvarez - edisonalaverzv10@gmail.com (28/05/2024)
"""

from ..engines_subsystem import Engine, EnginesFacade


# pylint: disable=too-few-public-methods
class EngineFlyweight:
    """
    This class represents the Flyweight for the Engines Sub-system.

    Attributes:
        __engines (dict): A dictionary with the engines.

    Methods:
        get_engine(Engine): This method returns an engine from the flyweight.
    """

    def __init__(self):
        self.__engines = {}

    def get_engine(self, engine_type: str, engine_price) -> Engine:
        """
        Retrieves an engine from the flyweight pool. If the engine does not exist in the pool,
        it is created using the EnginesFacade and then stored in the pool.

        Args:
            engine_type (str): The type of the engine to retrieve.
            engine_price (float): The price of the engine to retrieve.

        Returns:
            Engine: The requested engine, either retrieved from the pool or newly created.
        """
        if engine_type not in self.__engines:
            self.__engines[engine_type] = {}

        if engine_price not in self.__engines[engine_type]:
            self.__engines[engine_type][engine_price] = EnginesFacade.get_engine(
                engine_type, engine_price
            )

        return self.__engines[engine_type][engine_price]
