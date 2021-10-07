from random import randrange
from tombola import Tombola


@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    # issubclass: True
    print(f"issubclass: {issubclass(TomboList, Tombola)}")
    t = TomboList(range(100))
    # isinstance(t, Tombla), value: True
    print(f'isinstance(t, Tombla), value: {isinstance(t, Tombola)}')
