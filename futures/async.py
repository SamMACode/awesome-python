# -*- coding:utf-8 -*-
import asyncio

import aiohttp
import requests
import time
import concurrent.futures


def download_one(url):
	# requests.get(url)是线程安全的方法，不存在race condition
	resp = requests.get(url)
	print('Read {} from {}'.format(len(resp.content), url))
	# async with aiohttp.ClientSession() as session:
	# 	async with session.get(url) as resp:
	# 		print('Read {} from {}'.format(resp.content_length, url))


def download_all(url_sites):
	# solution 3: download data use asyncio.create_task，有些问题en.wikipedia地址无法访问
	# tasks = [asyncio.create_task(download_one(site)) for site in url_sites]
	# await asyncio.gather(*tasks)

	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		# solution 2: executor.map()会对sites中的每个url，分别调用download_one函数，max_workers默认用cpu数
		# executor.map(download_one, url_sites)
		to_do = []
		for site in url_sites:
			future = executor.submit(download_one, site)
			to_do.append(future)

		for future in concurrent.futures.as_completed(to_do):
			# executor.submit()后会产生future结果，as_completed()为异步判断是否执行完
			future.result()
	# solution 1: for site in url_sites:
	# 	download_one(site)


if __name__ == '__main__':
	sites = [
		'https://en.wikipedia.org/wiki/Portal:Arts',
		'https://en.wikipedia.org/wiki/Portal:History',
		'https://en.wikipedia.org/wiki/Portal:Society',
		'https://en.wikipedia.org/wiki/Portal:Biography',
		'https://en.wikipedia.org/wiki/Portal:Mathematics',
		'https://en.wikipedia.org/wiki/Portal:Technology',
		'https://en.wikipedia.org/wiki/Portal:Geography',
		'https://en.wikipedia.org/wiki/Portal:Science',
		'https://en.wikipedia.org/wiki/Computer_science',
		'https://en.wikipedia.org/wiki/Python_(programming_language)',
		'https://en.wikipedia.org/wiki/Java_(programming_language)',
		'https://en.wikipedia.org/wiki/PHP',
		'https://en.wikipedia.org/wiki/Node.js',
		'https://en.wikipedia.org/wiki/The_C_Programming_Language',
		'https://en.wikipedia.org/wiki/Go_(programming_language)'
	]
	start_time = time.perf_counter()
	download_all(sites)
	end_time = time.perf_counter()
	print("Download {} url_sites in {} seconds".format(len(sites), end_time - start_time))
