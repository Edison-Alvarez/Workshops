"""
This file contains the program of a new internal platform to define a vehicle catalog, for a vehicle construction company.

Author: Edison David Alvarez Varela
Date: Mar-15th-2024
"""

class Engine():
  def __init__(self, name, type_of_enginer, potency, weight):
    self.name = name
    self.type_of_engineer = type_of_enginer
    self.potency = potency
    self.weight = weight

class Chassis():
  def __init__(self, name, type_of_chassis, data_for_consumption):
    self.name = name
    self.type_of_chassis = type_of_chassis
    self.data_for_consumption = data_for_consumption

class Vehicle():
  def __init__(self, engine, chassis, model, year):
    self.engie = engine
    self.chassis = chassis
    self.model = model
    self.year = year

  def vehicle_gas_consumption(self):
    consumption = (self.engie.potency * 0,2) - (self.engie.weight * self.chassis.data_for_consumption)
    return consumption
    
class Car(Vehicle):
  def __init__(self, engine, chassis, model, year):
    super().__init__(engine, chassis, model, year)

class Truck(Vehicle):
  def __init__(self, engine, chassis, model, year):
    super().__init__(engine, chassis, model, year)
  
class Yacht(Vehicle):
  def __init__(self, engine, chassis, model, year):
    super().__init__(engine, chassis, model, year)
  
class Motorcycle(Vehicle):
  def __init__(self, engine, chassis, model, year):
    super().__init__(engine, chassis, model, year)

list_engines = []
list_vehicles = []
list_chassis = []

while True:
  print("BIENVENIDO A LA PLATAFORMA DE INVENTARIO DE VEHICULOS: \n (seleccione una opcion):")
  print("1. Crear un nuevo motor")
  print("2. Crear un nuevo vehiculo")
  print("3. Mostrar todos los vehículos registrados")
  print("4. Encontrar vehículo por año")
  print("5. Encontrar vehiculo por potencia del motor")
  print("6. Salir")

  opcion = int(input("Ingrese el número de la opción deseada: "))

  if opcion == 1:
    print("Ingrese los datos del motor:")
    name = input("Nombre: ")
    type_of_engineer = input("Tipo de motor: ")
    potency = float(input("Potencia: "))
    weight = float(input("Peso: "))
    engine = Engine(name, type_of_engineer, potency, weight)
    list_engines.append(engine)
    
  elif opcion == 2:
    print("Ingrese los datos del vehículo:")
    
    print("Seleccione el motor")
    
    for i in range(0, len(list_engines)):
      print(i+1,".", list_engines[i].name )
    motor_seleccionado = int(input("Ingrese el número del motor: "))
    engine = list_engines[motor_seleccionado]
    
    print("Seleccione el tipo de chasis")
    
    for i in range(0, len(list_chassis)):
      print(i+1,".", list_chassis[i].name)
    chasis_seleccionado = int(input("Ingrese el número del chasis: "))
    chassis = list_chassis[chasis_seleccionado]
    model = input("Modelo: ")
    year = int(input("Año: "))
    
    vehicle = Vehicle(engine, chassis, model, year)
    list_vehicles.append(vehicle)

  elif opcion == 3:
    print("Los vehiculos registrados son:")
    for i in range (0, len(list_vehicles)):
      print(i+1, ".", list_vehicles[i].name)

  elif opcion == 4:
    year = int(input("Ingrese el año: "))
    
    for i in range(0, len(list_vehicles)):
      if list_vehicles[i].year == year:
        print(list_vehicles[i].name)
        
  elif opcion == 5:
    potency = int(input("Ingrese la potencia: "))
    
    for i in range(0, len(list_vehicles)):
      if list_vehicles[i].engine.potency == potency:
        print(list_vehicles[i].name)
        
  elif opcion == 6:
    break

    
    
    