# “The collections.namedtuple function is a factory that produces subclasses of tuple enhanced with field names”
from random import shuffle
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])
City = namedtuple('City', 'name country population coordinates')


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# Named tuple attributes and methods (continued from the previous example)
def named_tuple_attributes():
    print(f"City.fields: {City._fields}")
    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.20889))
    # "_make() allow you to instantiate a named tuple from an iterable"
    delhi = City._make(delhi_data)
    # "can be used to produce a nice display of city data"
    delhi._asdict()
    for key, value in delhi._asdict().items():
        print(key + ':',  value)


# Press ⇧⌘F11 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⇧⌘B to toggle the breakpoint.


def set_card(deck, position, card):
    deck._cards[position] = card


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    tokyo = City('Tokyo', 'JP', 36.993, (35.689722, 139.691667))
    print(f'tokyo instance: {tokyo}')
    print_hi('PyCharm')
    print(f'tokyo.population: {tokyo.population}, tokyo.coordinates: {tokyo.coordinates}, tokyo[1]: {tokyo[1]}')
    named_tuple_attributes() 
    """

    deck = FrenchDeck()
#         x[i], x[j] = x[j], x[i]
# TypeError: 'FrenchDeck' object does not support item assignment
    FrenchDeck.__setitem__ = set_card
    shuffle(deck)
    print(f"after shuffle deck[:5]: {deck[:5]}")

