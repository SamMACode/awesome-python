from tombola import Tombola
import random


class Fake(Tombola):
    """declare Fake as a subclass of Tombola"""
    def pick(self):
        return 13


class BingoCage(Tombola):
    """BingoCage is a concrete class of Tombola"""
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


class LotteryBlower(Tombola):
    """LotteryBlower is a concrete subclass that overrides the inspect and loaded methods from Tomnola"""
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pickup from empty BingoCage')

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))
