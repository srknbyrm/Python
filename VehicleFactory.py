from DesignPatterns.Factory.Sedan import Sedan
from DesignPatterns.Factory.SUV import SUV
from DesignPatterns.Factory.Hatchback import Hatchback


class VehicleFactory:

    def generate(self, vehicle_type):
        if vehicle_type is 'Sedan':
            return Sedan().produce_vehicle()
        elif vehicle_type is 'SUV':
            return SUV().produce_vehicle()
        elif vehicle_type is 'Hatchback':
            return Hatchback().produce_vehicle()