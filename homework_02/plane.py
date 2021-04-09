"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
	def __init__(self, weight = 0, fuel = 0, fuel_consumption = 0, max_cargo = 0):
		super().__init__(weight, fuel, fuel_consumption)
		self.cargo = 0
		self.max_cargo = max_cargo

	def load_cargo(self, additional_cargo):
		# суммарный груз
		sum_cargo = self.cargo + additional_cargo

        # проверка на перегруз
		if sum_cargo <= self.max_cargo:
			self.cargo = sum_cargo
		else:
			raise CargoOverload

	def remove_all_cargo(self):
		# сохраним значание cargo
		cargo = self.cargo

		# обнулим cargo
		self.cargo = 0

		# возвратим значение до обнуления
		return cargo
