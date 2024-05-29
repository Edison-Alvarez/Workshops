"""
This file has some classes related to the implementation of an Abstract Factory Pattern Design..

Authors: Carlos Sierra - cavirguez@udistrital.edu.co / Edison Alvarez - edisonalaverzv10@gmail.com
Update: Edison Alvarez - edisonalaverzv10@gmail.com (28/05/2024)
"""

from abc import ABC, abstractmethod

from .engines import ElectricEngine, GasEngine, HybridEngine


class AbstractEngineFactory(ABC):
    """
    This class is an abstract factory to create both gas and electric engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create an electric engine.
        create_gas_engine -> GasEngine: This method create a gas engine.
        create_hybrid_engine -> HybridEngine: This method creates a hybrid engine.
    """

    @abstractmethod
    def create_electric_engine(self) -> ElectricEngine:
        """
        This method create an electric engine.

        Returns:
            An electric engine object.
        """

    @abstractmethod
    def create_gas_engine(self) -> GasEngine:
        """
        This method create a gas engine.

        Returns:
            A gas engine object.
        """

    @abstractmethod
    def create_hybrid_engine(self) -> HybridEngine:
        """
        This method create a hybrid engine.

        Returns:
            A hybrid engine object.
        """

class HighEngineFactory(AbstractEngineFactory):
    """
    This class is a concrete factory to create expensive versions of engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create an expensive electric engine.
        create_gas_engine -> GasEngine: This method create an expensive gas engine.
        create_hybrid_engine -> HybridEngine: This method creates a hybrid engine.
    """

    def create_electric_engine(self) -> ElectricEngine:
        """Creates an expensive electric engine."""
        return ElectricEngine(
            torque=180,
            maximum_speed=300,
            dimenssions="200x200x200",
            power=200,
            stability="high",
            weight=100.9,
        )

    def create_gas_engine(self) -> GasEngine:
        """Creates an expensive gas engine."""
        return GasEngine(
            torque=210,
            maximum_speed=400,
            dimenssions="210x200x250",
            power=250,
            stability="medium",
            weight=120.5,
        )

    def create_hybrid_engine(self) -> HybridEngine:
        """Creates an expensive hybrid engine."""
        return HybridEngine(
            torque=200,
            maximum_speed=350,
            dimensions="205x205x205",
            power=220,
            stability="high",
            weight=110.0,
            electric_power=150,
        )

class LowEngineFactory(AbstractEngineFactory):
    """
    This class is a concrete factory to create cheap versions of engines.

    Methods:
        create_electric_engine -> ElectricEngine: This method create a cheap electric engine.
        create_gas_engine -> GasEngine: This method create a cheap gas engine.
        create_hybrid_engine -> HybridEngine: This method creates a hybrid engine.
    """

    def create_electric_engine(self) -> ElectricEngine:
        """Creates a cheap electric engine."""
        return ElectricEngine(
            torque=90,
            maximum_speed=100,
            dimenssions="100x100x100",
            power=50,
            stability="low",
            weight=63.4,
        )

    def create_gas_engine(self) -> GasEngine:
        """Creates a cheap gas engine."""
        return GasEngine(
            torque=100,
            maximum_speed=150,
            dimenssions="110x100x150",
            power=100,
            stability="low",
            weight=80.5,
        )

    def create_hybrid_engine(self) -> HybridEngine:
        """Creates a cheap hybrid engine."""
        return HybridEngine(
            torque=95,
            maximum_speed=120,
            dimensions="105x105x105",
            power=70,
            stability="low",
            weight=70.0,
            electric_power=60,
        )
