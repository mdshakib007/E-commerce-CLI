from abc import ABC
from product import Product
from orders import *
from shop import *

class User(ABC):
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

class Seller(User):
    def __init__(self, name, address, username, password):
        super().__init__(name, username, password)
        self.address = address
    
    def show_my_products(self, shop):
        shop.show_my_products(self)

    def add_product(self, shop, product_name, price, quantity):
        shop.add_product(product_name, price, quantity, self)

    def remove_product(self, shop, product_name):
        shop.remove_product(product_name)


class Customer(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)
        self.cart = Order()

    def show_all_products(self, shop):
        shop.show_all_products()

    def my_cart(self):
        print("\n\tMy cart...")
        for product, quantity in self.cart.items.items():
            print(f"\tName: {product.name} - Quantity: {quantity} - Price: {product.price}")
        print(f"\tTotal Price: {self.cart.total_price}")

    def add_to_cart(self, shop, product_name, quantity):
        item = shop.find_product(product_name)
        if item:
            self.cart.add_item(shop, item, quantity)
        else:
            print(f"\n\t{product_name} not available in this shop!")
        
    def remove_from_cart(self, shop, product_name):
        self.cart.remove_item(shop, product_name)

    def place_order(self, amount):
        price = self.cart.total_price
        if amount < price:
            print("\n\tInsufficient amount!")
        else:
            self.cart.clear_cart()
            print(f"\n\t${price} paid successfully!")
            print(f"\tYour extra money: ${amount-price}")