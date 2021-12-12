from array import array
import math


class Vector2d:
    """methods so far are all special methods"""
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)


class Demo:
    """Comparing behaviors of classmethod and staticmethod"""
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


def vector2d_methods():
    """Vector2d instances have several representations"""
    v1 = Vector2d(3, 4)
    print(f"v1.x: {v1.x} v1.y: {v1.y}")
    x, y = v1
    # after unpack, x: 3.0, y: 4.0, v1: (3.0, 4.0)
    print(f"after unpack, x: {x}, y: {y}, v1: {v1}")
    v1_clone = eval(repr(v1))
    print(f"v1 == v1_clone: {v1 == v1_clone}, v1: {v1}, convert to bytes: {bytes(v1)}")


if __name__ == '__main__':
    vector2d_methods()
    # Demo.klassmeth: (<class '__main__.Demo'>,), Demo.klassmeth('spam'): (<class '__main__.Demo'>, 'spam'),
    # Demo.statmeth: ('spam',)
    print(f"Demo.klassmeth: {Demo.klassmeth()}, Demo.klassmeth('spam'): {Demo.klassmeth('spam')}, "
          f"Demo.statmeth: {Demo.statmeth('spam')}")
    