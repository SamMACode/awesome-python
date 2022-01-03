# -*- coding:utf-8 -*-
import os
import time

import psutil


def is_iterable(param):
	"""判断一个容器序列是否可迭代，iter(param)不抛出异常"""
	try:
		iter(param)
		return True
	except TypeError:
		return False


def show_memory_info(hint):
	"""显示当前python程序占用内存大小, hint为子程序名称"""
	pid = os.getpid()
	process = psutil.Process(pid)

	info = process.memory_full_info()
	memory = info.uss/ 1024. / 1024
	print("{} memory used: {} MB".format(hint, memory))


def test_iterator():
	show_memory_info('initing iterator')
	list_1 = [i for i in range(100000000)]
	show_memory_info('after iterator initiated')
	print(sum(list_1))
	show_memory_info('after sum function called')


def test_generator():
	show_memory_info('initiating generator')
	list_2 = (i for i in range(100000000))
	show_memory_info('after generator initiating')
	print(sum(list_2))
	show_memory_info('after sum called')


if __name__ == '__main__':
	params = [1234, '1234', [1, 2, 3, 4], set([1, 2, 3, 4]), {1: 1, 2: 2, 3: 3, 4: 4},
			(1, 2, 3, 4)]
	for param in params:
		print("{} is iterable? {}".format(param, is_iterable(param)))
	# 分别用iterator、generator创建数据集合，查看生成的列表数据
	start_time = time.time()
	test_iterator()
	print(">> initiating iterator which range 100000000, total used {} ms".format(time.time() - start_time))
	start_time = time.time()
	test_generator()
	print(f">> initiating generator, total used {time.time() - start_time} ms")
