from functools import reduce
from operator import add
import random
from inspect import signature


def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


# factorial(42): 1405006117752879898543142606244511569936384000000000, function doc: returns n!,
# type(factorial): <class 'function'>
print(f"factorial(42): {factorial(42)}, function doc: {factorial.__doc__}, "
      f"type(factorial): {type(factorial)}")
fact = factorial
factMap = map(factorial, range(11))
listValue = list(map(fact, range(11)))
# fact(5): 120, listValue: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
print(f"fact(5): {fact(5)}, factMap value: {factMap}, listValue: {listValue}")

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sortWithLength = sorted(fruits, key=len)
# ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']
print(f"sorted with length: {sortWithLength}")


def reverse(word):
    """define reverse method to reverse word spelling"""
    return word[::-1]


reverseArray = sorted(fruits, key=reverse)
# sort array by their reversed key: ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
print(f"reverse('testing'): {reverse('testing')}, reversed array: {reverseArray}")
factList = list(map(fact, range(6)))
factArray = [fact(n) for n in range(6)]
# factList: [1, 1, 2, 6, 24, 120], factArrat: [1, 1, 2, 6, 24, 120]
print(f"factList: {factList}, factArray: {factArray}")
lambdaFilter = list(map(factorial, filter(lambda n: n % 2, range(6))))
arrayFilter = [factorial(n) for n in range(6) if n % 2]
# lambdaFilter: [1, 6, 120], array filter: [1, 6, 120]
print(f"lambdaFilter: {lambdaFilter}, array filter: {arrayFilter}")

# use reduce and sum function to calculate data
# reduce(add, range(100)): 4950, sum(range(100)): 4950
print(f"reduce(add, range(100)): {reduce(add, range(100))}, sum(range(100)): {sum(range(100))}")


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
# bingo.pick(): 1, bingo(): 2, callable(bingo): True
print(f"bingo.pick(): {bingo.pick()}, bingo(): {bingo()}, callable(bingo): {callable(bingo)}")


# define class C and UDF func()
class C:
    pass


def func(): pass


obj = C()
# (dir(func) - dir(func) methods: ['__annotations__', '__call__', '__closure__', '__code__',
# '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
diff = sorted(set(dir(func)) - set(dir(obj)))
print(f"(dir(func) - dir(func) methods: {diff}")


def tag(name, *content, cls=None, **attrs):
    """generate one or more tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in
                           sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


# tag('br'): <br />, tag('p', 'hello'): <p>hello</p>, <p id="33">hello</p>
print(f"tag('br'): {tag('br')}, tag('p', 'hello'): {tag('p', 'hello')}, tag('p', 'hello', id=33): "
      f"{tag('p', 'hello', id=33)}")
# extract the function signature, such as tag function
sig = signature(tag)
# (name, *content, cls=None, **attrs), KEYWORD_ONLY : cls = None
print(f"signature of tag function: {sig}")
for name, param in sig.parameters.items():
    print(param.kind, ":", name, "=", param.default)

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
for name, value in bound_args.arguments.items():
    print(name, '=', value)
del my_tag['name']
# TypeError: missing a required argument: 'name'
# bound_args = sig.bind(**my_tag)

