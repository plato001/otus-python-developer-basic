"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """

    return [number ** 2 for number in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
	"""
	функция, которая проверяет явлется ли число простым
	"""
	
	if n <= 1 or n % 1 > 0:
		return False
	for i in range(2, n // 2 + 1):
  		if n % i == 0:
  			return False
	return True


def filter_numbers(list_of_numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    
    # создадим фильтр-функцию
    if filter_type == ODD:
    	filter_function = lambda x: x % 2 == 1
    elif filter_type == EVEN:
    	filter_function = lambda x: x % 2 == 0
    else:
    	filter_function = is_prime

    return list(filter(filter_function, list_of_numbers))