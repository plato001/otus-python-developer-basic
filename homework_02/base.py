from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight = 0, fuel = 0, fuel_consumption = 0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        # проверка состояния
        if not self.started:
            # проверка топлива
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        # остаток топлива, после прохождения расстояния distance
        fuel_residual = self.fuel - distance * self.fuel_consumption

        # проверяем, что остаток неотрицательный
        if fuel_residual >= 0:
            self.fuel = fuel_residual
        else:
            raise NotEnoughFuel
