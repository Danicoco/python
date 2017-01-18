class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.items = dict()

    def add_item(self, item_name, quantity, price):
        self.total += price * quantity
        self.items[item_name] = quantity
        
    def remove_item(self, item_name, quantity, price):
        if quantity > self.items[item_name]:
            self.items[item_name] = 0
        else:
            self.items[item_name] -= quantity
            self.total -= price * quantity
        
    def checkout(self, cash_paid):
        if self.total > cash_paid:
            return "Cash paid not enough"
        else:
            return (cash_paid - self.total)
            
class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100
    
    def remove_item(self):
        self.quantity -= 1