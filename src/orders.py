class Order:
    def __init__(self) -> None:
        self.items = {} #--> Product -> object : quantity -> int

    def add_item(self, shop, item, quantity):
        found = False
        for product in shop.products:
            if product == item:
                found = True
                if(product.quantity < quantity):
                    print(f"\n\tNot enough '{item.name}' to add!")
                else:
                    if item in self.items:
                        self.items[item] = quantity
                        print(f"\n\t'{item.name}' updated with quantity X{quantity}")
                    else:
                        self.items[item] = quantity
                        print(f"\n\t'{item.name}' X{quantity} added!")
                    product.quantity -= quantity
        if not found:
            print(f"'{item.name}' not found!")
    
    def remove_item(self, shop, item_name):
        found = False
        for product in shop.products:
            if product.name == item_name:
                for item, quan in self.items.items():
                    if item.name == item_name:
                        found = True
                        product.quantity += quan
                        del self.items[item]
                        print(f"\n\t'{item_name}' deleted from cart!")
                        break
                if found: break
        
        if not found:
            print(f"\n\t'{item_name}' not found!")
        

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear_cart(self):
        self.items = {}


