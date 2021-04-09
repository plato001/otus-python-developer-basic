"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
	def __init__(self, weight = 0, fuel = 0, fuel_consumption = 0):
		super().__init__(weight, fuel, fuel_consumption)
		self.engine = None

	def set_engine(self, engine: Engine):
		"""
		Метод принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car
		"""

		self.engine = engine
