import os
import bisect
import sys
from array import array
from random import random
import numpy


def filterData():
    """Build a list of Unicode codepoints from a string, filter data use lambda expression"""
    symbols = '$¢£¥€¤'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    # “more readable because its intent is explicit”
    sort_codes = [ord(symbol) for symbol in symbols]
    print(f"all items in codes are: {codes}, sort_codes value: {sort_codes}")

    # listcomps do everything the map and filter functions do
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(f"all the character which beyond 127 are: {beyond_ascii}")
    # use python lambda expression
    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(f"use lambda expression to filter character which beyond 127 are: {beyond_ascii}")


def foreach():
    """Cartesian product using a list comprehension"""
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(f"use Cartesian operators, value: {tshirts}")
    # “uses a genexp with a Cartesian product to print out a roster of T-shirts of two colors in three sizes”
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(f"{tshirt}")


def unpackTuple():
    """Tuples used as records, for loop statement"""
    lax_coordinates = (33.9425, -118.408056)
    # tuple unpacking
    latitude, longitude = lax_coordinates
    print(f"latitude: {latitude}, longitude: {longitude}")
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    traveler_ids = [('USA', '31195885'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)
    for country, _ in traveler_ids:
        print(country)

    # “the os.path.split() function builds a tuple (path, last_part) from a filesystem path:”
    _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
    print(f'operation system filename: {filename}')
    # Using * to grab excess times
    a, b, *rest = range(5)
    print(f'a: {a}, b: {b}, rest: {rest}')
    a, *body, c, d = range(5)
    print(f'a: {a}, body: {body}, c: {c}, d: {d}')
    *head, b, c, d = range(5)
    print(f'head: {head}, b:{b}, c:{c}, d:{d}')


def beautifyArray():
    """Nested tuple Unpacking, unpacking nested tuples to access the longitude"""
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
    ]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(fmt.format(name, latitude, longitude))


def splitArray():
    l = [10, 20, 30, 40, 50, 60]
    # l[:2] value: [10, 20], l[2:] value: [30, 40, 50, 60]ß
    print(f"l[:2] value: {l[:2]}, l[2:] value: {l[2:]}")
    l = list(range(10))
    print(f"list(range(10)): {l}")
    l[2:5] = [20, 30]
    del l[5:7]
    print(f"after del l[5:7], l items are: {l}")
    # building lists of lists
    board = [['_'] * 3 for i in range(3)]
    board[1][2] = 'X'
    print(f"two dimension array value: {board}")
    weird_board = [['_'] * 3] * 3
    # The outer list is made of three references to the same inner list. While it is unchanged, all seems right
    weird_board[1][2] = '0'
    # [['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]
    print(f"weird_board value: {weird_board}")


def sortedData():
    # list.sort and sorted take two optional, keyword-only arguments
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(f"sorted(fruits): {sorted(fruits)} , origin array: {fruits}")
    # sort array item by item.length
    print(f"sorted by element length: {sorted(fruits, key=len, reverse=True)}")

    # Creating, saving, and loading a large array of floats
    floats = array('d', (random() for i in range(10 ** 7)))
    print(f'floats[-1]: {floats[-1]}')
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()
    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10 ** 7)
    fp.close()
    print(f'floats2 value: {floats2}, whether floats2 == floats: {floats2 == floats}')


def memoryView():
    # memoryView
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(f"len(memv): {len(memv)}, memv[0]: {memv[0]}")
    memv_oct = memv.cast('B')
    print(f"memv_oct value: {memv_oct.tolist()}")
    memv_oct[5] = 4
    print(f"after memv_oct[5] = 4, numbers: {numbers}")

    # basic operations with rows and columns in a numpy.ndarray
    array = numpy.arange(12)
    print(f"numpy_array: {array}, type(array): {array}")
    array.shape = 3, 4
    print(f"after shape(3, 4), array: {array}, array[2]: {array[2]}")


def demo(bisect_fn):
    """bisect and insort—that use the binary search algorithm to quickly find and insert items"""
    # in any sorted sequence
    HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
    ROW_FORMAT = "{0:2d} @ {1:2d} {2}{0:<2d}"
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FORMAT.format(needle, position, offset))


if __name__ == '__main__':
    # if sys.argv[-1] == 'left':
    #     bisect_fn = bisect.bisect_left
    # else:
    #     bisect_fn = bisect.bisect
    # print('DEMO: ', bisect_fn.__name__)
    # print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    # demo(bisect_fn)

    # 创建新的元组new_tup，并依次填充原数组的值
    tup = (1, 2, 3, 4)
    new_tuple = tup + (5, )
    print(f"new tuple data: {new_tuple}, list convert: {list(new_tuple)}")
