from structural.adapter.car_example.car import Car
from structural.adapter.car_example.motorcycle import Motorcycle


class MotorcycleAdapter(Car, Motorcycle):

    def __init__(self):
        super().__init__()

    def accelerate(self):
        self.rev_throttle()

    def apply_brakes(self):
        self.pull_brake_lever()

    def assign_driver(self, name):
        self.assign_rider(name)
