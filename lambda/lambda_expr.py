# -*- coding:utf-8 -*-
from functools import reduce


MAX_VALUE = 23  # define global variable and use with global syntax


def find_largest_element(l = [8, 0, -2, 3]):
	"""find the largest element in list, param must not be empty"""
	if not isinstance(l, list):
		print("input is not type of list")
		return
	if len(l) == 0:
		print("empty list")
		return
	largest_element = l[0]
	for item in l:
		if item > largest_element:
			largest_element = item
	global MAX_VALUE
	print(f"largest element is: {largest_element}, global value: {MAX_VALUE}")


def nth_power(exponent):
	"""定义闭包函数，nth_power返回值为exponent_of()函数"""
	def exponent_of(base):
		return base ** exponent
	return exponent_of


def map_reduce_func():
	"""函数式编程优点：其纯函数和不可变特性使程更健壮"""
	array = [1, 2, 3, 4, 5]
	map_list = map(lambda x: x * 2, array)  # [2， 4， 6， 8， 10]
	filter_elems = filter(lambda x: x % 2 == 0, array)
	print(f"map function: {map_list}, filter function: {filter_elems}")
	reduce_value = reduce(lambda x, y: x * y, array)  # 1*2*3*4*5 = 120
	print(f"reduce result: {reduce_value}")


if __name__ == '__main__':
	# largest element is: 8
	find_largest_element([8, -1, 3, 2, 7])
	# 通过闭包定义计算数平方、立方的function, 函数方法调用较为简单（匿名函数）
	square = nth_power(2)
	cube = nth_power(3)
	# square(2): 4, cube(2): 8
	print(f"square(2): {square(2)}, cube(2): {cube(2)}")

	# define list of tuple element, use lambda expression to sort tuple._2
	array = [(1, 20), (3, 0), (9, 10), (2, -1)]
	array.sort(key=lambda x: x[1])
	# after sort logical, array elements: [(2, -1), (3, 0), (9, 10), (1, 20)]
	print(f"after sort logical, array elements: {array}")
	map_reduce_func()

	d = {'mike': 10, 'lucky': 2, 'ben': 30}
	result = sorted(d.items(), key=lambda x: x[1], reverse=True)
	# after sorted by value, result is: [('ben', 30), ('mike', 10), ('lucky', 2)]
	print(f"after sorted by value, result is: {result}")
