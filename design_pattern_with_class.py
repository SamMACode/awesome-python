from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# the Strategy: an abstract base class, Promotion as an abstract base class (ABC)
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion):  # first concrete strategy
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # second concrete strategy
    """10% discount for each lineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # third strategy
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


if __name__ == '__main__':
    # two customers: joe has 0 fidelity points, ann has 1000
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]

    joe_order = Order(joe, cart, FidelityPromo())
    ann_order = Order(ann, cart, FidelityPromo())
    # joe's order: <Order total: 42.00 due: 42.00>, ann's order: <Order total: 42.00 due: 39.90>
    print(f"joe's order: {joe_order}, ann's order: {ann_order}")

    banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
    joe_bulk_order = Order(joe, banana_cart, BulkItemPromo())
    # joe_bulk_order: <Order total: 30.00 due: 28.50>
    print(f"joe_bulk_order: {joe_bulk_order}")

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    joe_large_order = Order(joe, long_order, LargeOrderPromo())
    joe_cart_order = Order(joe, cart, LargeOrderPromo())
    # joe's large order: <Order total: 10.00 due: 9.30>, joe's cart order: <Order total: 42.00 due: 42.00>
    print(f"joe's large order: {joe_large_order}, joe's cart order: {joe_cart_order}")

