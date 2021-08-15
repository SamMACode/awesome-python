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
