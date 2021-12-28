# -*- coding:utf-8 -*-
import time
import asyncio


async def crawl_page(url):
	"""依据url中截取的时间，通过time.sleep(seconds)api进行休眠"""
	print('crawling {}'.format(url))
	sleep_time = int(url.split('_')[-1])
	await asyncio.sleep(sleep_time)
	print("Ok {}".format(url))


async def metrics():
	"""用time()api来测试python代码执行的效率, asyncio.create_task()异步任务"""
	start_time = time.time()
	urls = ['url_1', 'url_2', 'url_3', 'url_4']
	tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
	# for task in tasks:
	# 	await task
	# 另一种写法，asyncio.gather(*tasks)会等到所有task都跑完
	await asyncio.gather(*tasks)
	print(f"total used {round(time.time() - start_time, 2)} s for crawling webpage")


if __name__ == '__main__':
	asyncio.run(metrics())
