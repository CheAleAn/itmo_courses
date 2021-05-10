class Ingredient(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.cost = cost
        self.weight = weight

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_weight(self):
        return self.weight


class Pizza(object):
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, other):
        self.ingredients.append(other)

    def get_name(self):
        return self.name

    def get_cost(self):
        return sum(i.get_cost() for i in self.ingredients)

    def get_weight(self):
        return sum(i.get_weight() for i in self.ingredients)/1000


class Order(object):
    def __init__(self):
        self.receipt = []

    def get_cost(self):
        return sum(i.get_cost() for i in self.receipt)

    def add_pizza(self, other):
        self.receipt.append(other)

    def print_receipt(self):
        for i in self.receipt:
            print(f'{i.get_name()} ({(i.get_weight()):.3f}г) - {(i.get_cost()):.2f}руб')
