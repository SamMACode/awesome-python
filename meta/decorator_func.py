# -*- coding:utf-8 -*-
import functools


def repeat(num):
	def my_decorator(func):
		"""当被装饰的函数有多个参数时，可以用*args、**kwargs进行调用"""
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			for i in range(num):
				print('wrapper of decorator')
				func(*args, **kwargs)
		return wrapper
	return my_decorator


@repeat(4)
def greet():
	"""python语法糖，通过annotation对function进行包装"""
	print("hello world")


class Count:
	"""类装饰器，主要依赖于函数__call__，每当调用一个类的示例时，call()函数就会被调用一次"""
	def __init__(self, func):
		self.func = func
		self.num_calls = 0

	def __call__(self, *args, **kwargs):
		self.num_calls += 1
		print("mum of calls is {}".format(self.num_calls))
		return self.func(*args, **kwargs)


@Count
def example():
	print("hello world")


if __name__ == '__main__':
	# console output: wrapper of decorator, hello world
	# @my_decorator语法相当于greet=my_decorator(greet)，只不过写法更加简洁
	greet()
	# func name: wrapper, 为了保持原函数，使用@functools.wraps(func)修饰wrapper函数
	print(f"func name: {greet.__name__}")
	# mum of calls is 1, hello world
	example()