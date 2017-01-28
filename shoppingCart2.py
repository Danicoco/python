class ShoppingCart:
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):

        self.items[item_name] = self.items.get(item_name, 0) + quantity
        self.total += (price*quantity)

    def remove_item(self,item_name, quantity, price):
        if not item_name in self.items:
            return 'item not in cart'
        elif quantity > self.items[item_name]:
            self.total -= (price * self.items[item_name])
            del(self.items[item_name])

        elif quantity < self.items[item_name]:
            self.items[item_name] = self.items.get(item_name, 0) - quantity
            self.total -= (price*quantity)
        else:
            del (self.items[item_name])
            self.total -= (price * quantity)

    def checkout(self, cashpaid):
        if cashpaid < self.total:
            return 'Cash paid not enough'
        else:
            balance = cashpaid - self.total
            return balance


class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1
