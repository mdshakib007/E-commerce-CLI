class Product:
    def __init__(self, name, price, quantity, seller) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.seller = seller #--> it's an instance of Seller class
    