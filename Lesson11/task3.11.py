# Task 3
# Product Store

from typing import Dict


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.type}\t{self.name}'


class ProductStore:
    mark_up: int
    store: Dict

    def __init__(self, name, mark_up):
        self.name = name
        self.mark_up = mark_up
        self.store = {}
        self.moneys = 0

    def add_product(self, prod: Product, count: int):
        self.store.update({prod: {'count': count, 'price': self.__calc_price(prod.price)}})

    def display(self):
        print(f'Product store {self.name}. In cash register we have {self.moneys} $')
        for prod, value in self.store.items():
            prod: Product
            value: Dict
            print(prod, value)

    def __calc_price(self, price):
        return round(price * (1 + self.mark_up / 100), 2)

    def __get_prod(self, name):
        for prod in self.store:
            if prod.name == name:
                return prod
        return None

    def sell(self, prod_name, prod_count):
        prod = self.__get_prod(prod_name)
        if prod and self.store[prod]['count'] >= prod_count:
            self.store[prod]['count'] -= prod_count
            self.moneys += self.store[prod]['price'] * prod_count


if __name__ == '__main__':
    p1 = Product('bakery', 'cinnamon_roll', 10)
    p2 = Product('fruits', 'lemon', 2)

    st1 = ProductStore('Wholefoods', 30)
    st2 = ProductStore('Walmart', 10)

    st1.add_product(p1, 40)
    st2.add_product(p1, 50)
    st1.add_product(p2, 25)
    st2.add_product(p2, 80)

    st1.display()
    st2.display()
    print('-' * 40)

    st1.sell('cinnamon_roll', 10)
    st2.sell('cinnamon_roll', 8)

    st1.display()
    st2.display()
