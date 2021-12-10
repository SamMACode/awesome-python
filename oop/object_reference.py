import copy
import weakref


class Bus:
    """Defines a simple class ~ Bus, representing a school bus that is loaded with passengers"""
    def __init__(self, passengers):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def bye():
    print('Gone with the wind...')


class Cheese:
    """Cheese has a kind attribute and a standard representation"""
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


if __name__ == '__main__':
    # charles and lewis refer to the same object
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    print(f"lewis = charles: {lewis is charles}")
    lewis['balance'] = 950
    # id(charles): 140257173710720, id(lewis): 140257173710720, charles: {'balance': 950}
    print(f"id(charles): {id(charles)}, id(lewis): {id(lewis)}, charles['balance']: {charles['balance']}")
    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    # is operator is used to compare id(object), == only compare field value
    print(f"charles is alex: {charles is alex}, charles equals charles: {charles == alex}")

    # list() method only shallow copy items, append 100 to l1
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)
    l1.append(100)
    l1[1].remove(55)
    # l1 items [...(7, 8, 9), 100], l2 items don't change
    print(f"l1 values: {l1}, l2 items: {l2}")
    l2[1] += [33, 22]
    l2[2] += (10, 11)
    print(f"l1 values: {l1}, l2 items: {l2}")

    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    # bus1: 140590744738160, bus2: 140590764696048, bus3: 140590764697344
    print(f"bus1: {id(bus1)}, bus2: {id(bus2)}, bus3: {id(bus3)}")
    bus1.drop('Bill')
    # bus2.passengers: ['Alice', 'Claire', 'David'], bus2.passengers: ['Alice', 'Bill', 'Claire', 'David']
    print(f"bus2.passengers: {bus2.passengers}, bus2.passengers: {bus3.passengers}")

    s1 = {1, 2, 3}
    s2 = s1
    ender = weakref.finalize(s1, bye)
    print(f"ender.alive: {ender.alive}")
    del s1
    s2 = 'spam'
    # after del s1 and reset s2 to spam, ender.alive: False
    print(f"after del s1 and reset s2 to spam, ender.alive: {ender.alive}")

    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(f"sorted(stock.keys): {sorted(stock.keys())}")
    del catalog
    # after delete catalog, sorted(stock.keys): ['Parmesan'], temporary variable cheese may cause an object to
    # last longer than expected by holding a reference to it
    print(f"after delete catalog, sorted(stock.keys): {sorted(stock.keys())}")
    del cheese
    print(f"delete cheese, sorted(stock.keys): {sorted(stock.keys())}")