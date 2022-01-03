# -*- coding:utf-8 -*-
import multiprocessing
import time


def cpu_bound(number):
	return sum(i * i for i in range(number))


def find_sums(numbers):
	# multiprocessing.Pool()会创建进程池，将cpu_bound函数、数据作为key/value进行计算
	with multiprocessing.Pool() as pool:
		pool.map(cpu_bound, numbers)


if __name__ == '__main__':
	numbers = [10000000 + x for x in range(20)]
	start_time = time.time()
	find_sums(numbers)
	duration = time.time() - start_time
	# find sums total use 5.190863847732544 seconds
	print(f"find sums total use {duration} seconds")