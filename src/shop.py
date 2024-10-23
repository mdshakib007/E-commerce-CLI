from product import Product
from users import Seller, Customer

class Shop:
    '''This class maintain all the application related to Shop'''
    def __init__(self, name) -> None:
        self.name = name
        self.customers = [] #--> instance of Customer class
        self.sellers = []   #--> instance of Seller class
        self.products = []  #--> instance of Product class

    def seller_register(self, name, address, username, password):
        for seller in self.sellers:
            if seller.username == username:
                print("\n\tThis username is already taken!")
                return None
        
        seller = Seller(name, address, username, password)
        self.sellers.append(seller)
        print("\n\tRegistration Successful!")
        return seller

    def seller_login(self, username, password):
        for seller in self.sellers:
            if seller.username == username and seller.password == password:
                print("\n\tLogin successfun!")
                return seller
        print("\n\tIncorrect username or password!")
        return None

    def customer_register(self, name, username, password):
        for customer in self.customers:
            if customer.username == username:
                print("\n\tThis username is already taken!")
                return None
        
        customer = Customer(name, username, password)
        self.customers.append(customer)
        print("\n\tRegistration Successful!")
        return customer

    def customer_login(self, username, password):
        for customer in self.customers:
            if customer.username == username and customer.password == password:
                print("\n\tLogin successfun!")
                return customer
        print("\n\tIncorrect username or password!")
        return None

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def add_product(self, product_name, price, quantity, seller): #-->  'product' is instance of Product class
        product = Product(product_name, price, quantity, seller)
        prod = self.find_product(product.name)
        found = False
        if prod:
            found = True
            self.products.remove(prod)
        self.products.append(product)
        
        if found:
            print(f"\n\t{product_name} updated with quantity {quantity}!")
        else:
            print(f"\n\t{product_name} added!")

    def remove_product(self, product_name):
        prod = self.find_product(product_name)
        if prod:
            self.products.remove(prod)
            print(f"\n\t{product_name} removed!")
        else:
            print(f"\n\t{product_name} not found!")

    def show_all_products(self):
        print("\n\tAll available products...")
        for product in self.products:
            print(f"\tName: {product.name} - Price: {product.price} - Quantity: {product.quantity} - Seller: {product.seller.name}")

    def show_my_products(self, seller):
        print("\n\tMy products...")
        for product in self.products:
            if product.seller == seller:
                print(f"\tName: {product.name} - Price: {product.price} - Quantity: {product.quantity} - Seller: {product.seller.name}")