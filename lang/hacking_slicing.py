import math
import numbers
import reprlib
from array import array
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])


class Vector:
    typecode = 'd'

    def __init__(self, components):
        # self._components is protected attribute
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        """
        use reprlib.repr() to get limited-length representation of self._components，
        (e.g., array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...]))
        """
        components = reprlib.repr(self._components)
        components = components[components.find(['[']):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # we pass the memoryview directly to the constructor, without unpacking with *
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyz'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = "readonly attribute {attr_name!r}"
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''

            # if there is nonblank error message, raise AttributeError
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)


if __name__ == '__main__':
    v1 = Vector([3, 4, 5])
    print(f"len(v1): {len(v1)}, v1[0]: {v1[0]}, v1[-1]: {v1[-1]}")
    v7 = Vector(range(7))
    # print(f"v7[1:4]: {v7[1:4]}, v7[1, 2] cause TypeError {v7[1,2]}")
    # set attribute to Vertex object (v.x = 10)
    v = Vector(range(5))
    v.x = 10
    # v 4 dimension values: (0.0, 1.0, 2.0, 3.0, 4.0), v.x: 10
    print(f"v 4 dimension values: {v}, v.x: {v.x}")
