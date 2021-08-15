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
`python`对两个数组计算笛卡尔积，通过两个`for`语句从`array`中提取元素，然后进行自由组合：
```python
# “Cartesian product using a list comprehension”
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
```
`range(value)`函数会生成从`0`~`value`间的整数数组，`*variable`会将除`index`为`0`和`1`的元素赋予`variable`：
```python
# a: 0, b: 1, rest: [2, 3, 4]
a, b, *rest = range(5)

l = [10, 20, 30, 40, 50, 60]
# l[:2] value: [10, 20], l[2:] value: [30, 40, 50, 60]ß
print(f"l[:2] value: {l[:2]}, l[2:] value: {l[2:]}")
del l[5:7]  # remove 5~7 element from array
```
`python`中的`dictionary`本质上为`map`，按`(key, value)`的格式存储数据，既可以用`one = 1`，也可以用`json`类似结构，`zip`函数作用与`scala`中相同：
```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
```
可用`MappingProxyType`创建一个只读`map`，修改`dict`元素值时会抛出异常：
```python
# using MappingProxyType builds a read-only mapping-proxy instance from a dict
maps = {1: 'A'}
d_proxy = MappingProxyType(maps)
'''
    d_proxy[2] = 'X'
TypeError: 'mappingproxy' object does not support item assignment
d_proxy[2] = 'X'
'''
maps[2] = 'B'
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
`python`中的类由`class`关键字或`namedtuple`来定义，其中`__init__`类似于`constructor function`：
```python
Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity
```
