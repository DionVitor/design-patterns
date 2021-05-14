"""Baseado no livro Python Fluente, Luciano Ramalho."""
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')
a = namedtuple('int', 'name')


class LineItem:
    def __init__(self, product, quantity, price):
        self.__product = product
        self.__quantity = quantity
        self.__price = price

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.__customer = customer
        self.__cart = cart
        self.__promotion = promotion

    @property
    def customer(self):
        return self.__customer

    @property
    def cart(self):
        return self.__cart

    @property
    def promotion(self):
        return self.__promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.__promotion is None:
            discount = 0
        else:
            discount = self.__promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order by {self.customer.name}. Total: {self.total():.2f}, due: {self.due():.2f}>'


class Promotion(ABC):  # Strategy: uma classe-base abstrata

    @abstractmethod
    def discount(self, order):
        """Devolver o desconto como um valor positivo em dólares"""


class FidelityPromo(Promotion):  # Primeira estratégia concreta
    """5% de desconto para clientes com mil ou mais pontos no programa de fidelidade."""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # Segunda estratégia concreta
    """10% de desconto para cada LineItem com 20 ou mais unidades"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # Terceira estratégia concreta
    """"7% de desconto para pedidos com 10 ou mais itens diferentes"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}

        if len(distinct_items) >= 10:
            return order.total() * .07

        return 0


dion = Customer('Dion Vitor', 0)
fernanda = Customer('Fernanda', 1100)

cart = [LineItem('banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5.0)]

print(Order(dion, cart, FidelityPromo()))
print(Order(fernanda, cart, FidelityPromo()))

banana_cart = [LineItem('banana', 30, 0.5), LineItem('apple', 10, 1.5)]

print(Order(dion, banana_cart, BulkItemPromo()))
print(Order(fernanda, banana_cart, BulkItemPromo()))

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

print(Order(dion, long_order, LargeOrderPromo()))
print(Order(dion, cart, LargeOrderPromo()))
