# -*- coding:utf-8 -*-
import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup


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


async def fetch_content(url):
	"""通过url从豆瓣网来抓取数据，async、await来等待response.text()结束"""
	async with aiohttp.ClientSession(
			headers={'users-agent': 'Mozilla/5.0'}, connector=aiohttp.TCPConnector(ssl=False)
	) as session:
		async with session.get(url) as response:
			return await response.text()


async def use_bs4_fetch_data():
	"""通过beautiful_Soup4解析python爬到的数据，从doc中解析缩略图"""
	url = "https://movie.douban.com/cinema/later/beijing/"
	init_page = await fetch_content(url)
	init_soup = BeautifulSoup(init_page, 'lxml')

	movie_names, urls_to_fetch, movie_dates = [], [], []
	all_movies = init_soup.find('div', id='showing-soon')
	for each_movie in all_movies.find_all('div', class_="item"):
		all_a_tag = each_movie.find_all('a')
		all_li_tag = each_movie.find_all('li')

		# 从<a>链接中提取href、date日期、tag#text中影片名称，并通过printf打印console
		movie_names.append(all_a_tag[1].text)
		urls_to_fetch.append(all_a_tag[1]['href'])
		movie_dates.append(all_li_tag[0].text)
	tasks = [fetch_content(url) for url in urls_to_fetch]
	pages = await asyncio.gather(*tasks)

	for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
		soup_item = BeautifulSoup(page, 'lxml')
		img_tag = soup_item.find('img')
	# 穿过寒冬拥抱你 12月31日 https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2801718909.jpg
	# 以年为单位的恋爱 12月31日 https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2715903096.jpg
		print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


if __name__ == '__main__':
	# asyncio.run(metrics())
	asyncio.run(use_bs4_fetch_data())
