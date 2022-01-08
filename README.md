# Python grammer
> “Python is an easy to learn, powerful programming language.” Those are the first words of the official Python Tutorial. Python语言广泛应用在数据分析、机器学习、大数据计算（PySpark）等领域，通过读 `Fluent Python`学习下它的语法。

### Python基本变量类型
`python`一共定义了`5`个标准的数据类型：`Number`、`String`、`List`、`Tuple`和`Dictionary`，给变量赋值时不需声明类型，`python`会自动依据值做判断。
```python
# drink被识别为string，price为float浮点类型
drink = 'café'
price = 10.5
# array中元素类型可不一致，tuple、float、string都可以，获取元素用array[index]
city_info = ['newyork', 23, 10.34, (35.689722, 139.691667)]
```
遍历`array`中元素的不同写法，`for`和`lambda`对`array`完成遍历、元素筛选（过滤`ascii`码大于`127`的字符）：
```python
symbols = ['o', '0', '¢', '£', '¥', '€', '¤']
# listcomps do everything the map and filter functions do
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

# use python lambda expression
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
```
`python`对两个数组计算笛卡尔积，通过两个`for`语句从`array`中提取元素，然后进行自由组合，`range(value)`函数会生成从`0`~`value`间的整数数组：
```python
# “Cartesian product using a list comprehension”
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# a: 0, b: 1, rest: [2, 3, 4]
a, b, *rest = range(5)
```
### function及class的定义
通过`def`关键来定义函数，不需定义函数的返回类型，`function.__doc__`能获取函数的说明：
```python
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)

# factorial(42): 1405006117752879898543142606244511569936384000000000, function doc: returns n!,
# type(factorial): <class 'function'>
print(f"factorial(42): {factorial(42)}, function doc: {factorial.__doc__}, "
        f"type(factorial): {type(factorial)}")
```
`python`中的类由`class`关键字来定义，其中`__init__`类似于`constructor function`，在`class`定义中`@classmethod`修饰类函数、`@staticmethod`修饰静态函数：
```python
class Document():
  WELCOME_STR = 'Welcome! The context for this book is {}.'
  def __init__(self, title, author, context):
    print('init function called')
    self.title = title
    self.author = author
    self.__context = context
```
`python`中通过`class BOWInvertedIndexEngine(SearchEngineBase)`来实现继承，基类`class`作为参数放入派生类中，`__init__(self)`函数中先调用父类的构造函数:
```python
class BOWInvertedIndexEngine(SearchEngineBase):
  def __init__(self):
    super(BOWInvertedIndexEngine, self).__init__()
    self.inverted_index = {}
```
用`lambda`语法实现`map-reduce`函数，和其它语言一样，匿名函数写法简洁、可读性好：
```Python
array = [1, 2, 3, 4, 5]
map_list = map(lambda x: x * 2, array)  # [2， 4， 6， 8， 10]
reduce_value = reduce(lambda x, y: x * y, array)  # 1*2*3*4*5 = 120
```
### 并发、多线程数据处理
一般用`asyncio`的`create_task()`来创建任务，并通过`await`等待任务执行完成、或者使用`asyncio.gather(*task)`等待任务执行完成：
```python
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
```
并行执行`futures`特性，当执行`task`需获取返回结果时，`futures`中的方法`done()`，表示相对应的操作是否完成-`True`表示完成，`False`表示没有完成。
```Python
def download_all(url_sites):
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
```
`python`中的多进程组件在`multiprocessing`包下，使用方式也较为简单，创建多进程池，通过`pool.map()`执行`task`：
```python
def find_sums(numbers):
  # multiprocessing.Pool()会创建进程池，将cpu_bound函数、数据作为key/value进行计算
  with multiprocessing.Pool() as pool:
    pool.map(cpu_bound, numbers)
```
