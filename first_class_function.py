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

