class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        counter = 0
        while counter < quantity:
            self.items.append({'name':name, 'price':price})
            counter += 1
            self.total += price                                
        return self.total

    def mean_item_price(self):
        num_items = len(self.items)
        total = self.total
        mean = total/num_items
        return mean

    def median_item_price(self):
        price_list = sorted([i['price'] for i in self.items])
        median = 0
        if len(price_list) % 2 == 0:
            median = (price_list[(len(price_list)/2) - 1] + price_list[(len(price_list)/2) + 1]) / 2
        else:
            median = price_list[int((len(price_list)+1 / 2) - 1)]
        return median
                                 

    def apply_discount(self):
        if self.employee_discount:
            disc = self.total - (int(self.total * (self.employee_discount/100)))
            return disc
        else:
            return 'Sorry, there is no discount to apply for this cart.'

    def void_last_item(self):
        if len(self.items) > 0:
            self.total -= self.items[-1]['price']
            self.items.pop()
        else:
            return 'There are no items in your cart!'
        