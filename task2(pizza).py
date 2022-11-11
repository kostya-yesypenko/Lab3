from datetime import datetime

pizzas_of_the_day = [
    ['Salami', 'Tomatoes', 'Cheese'],
    ['Chicken', 'Pineapples', 'Corn'],
    ['Tomatoes', 'Cheese', 'Pepper'],
    ['Beef' 'Tomatoes', 'Cheese'],
    ['Shrimps', 'Squids', 'Olives'],
    ['Beef', 'Mushrooms', 'Tomatoes'],
    ['Salami', 'Mushrooms', 'Pepper']
]


prices = {
    'Tomatoes': 2, 'Salami': 3, 'Cheese': 3, 'Olives': 4, 'Chicken': 3, 'Pineapples': 5, 'Corn': 2,
    'Pepper': 2, 'Bacon': 3, 'Shrimps': 6, 'Squids': 8, 'Beef': 5, 'Mushrooms': 3
}


class Pizza:
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], list):
            self.piza = args[0]
        else:
            self.piza = []
            for ingredient in args:
                self.piza.append(ingredient)
        self.additive = kwargs.get('add')
        self.price = self.order()


    def order(self):
        price = 0
        for ing in self.piza:
            price += prices.get(ing)
        new_add = []
        if self.additive:
            for ing in self.additive:
                try:
                    price += prices.get(ing)
                    new_add.append(ing)
                except TypeError:
                    pass
        self.additive = new_add
        return price


    def get_price(self):
        return self.price

    def __str__(self):
        based = ''
        for ing in self.piza:
            based += ing + '\n'
        add = ''
        for ing in self.additive:
            add += ing + '\n'
        if add == '':
            add += 'No additive\n'
        out = "You ordered pizza with:\n" + based + "Additive:\n" + add
        return out


class PizzaOfTheDay(Pizza):
    def __init__(self, *args):
        today = pizzas_of_the_day[datetime.today().weekday()]
        super().__init__(today, add=args)


p1 = PizzaOfTheDay()
p2 = PizzaOfTheDay('Mushrooms')
p3 = Pizza('Cheese', 'Mushrooms')

print(p1)
print(p2)
print(p3)
f'Price of 3 pizza is', p3.get_price()
