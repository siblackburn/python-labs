'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class treats():
    total_market_value = 0
    total_market_volume = 0

    def __init__(self, category, market_value = 0, average_price = 0.0):
        self.category = category
        self.market_value = market_value
        self.average_price = average_price
        self.volume = market_value / average_price # Think this may be broken. Open up debugger to find out, the use divide dunder to fix
        treats.total_market_value += market_value
        treats.total_market_volume += self.volume

    def __str__(self):
        return f'The {treats.category} has a market value of {treats.market_value} with an average price per unit of {treats.average_price}'

    @staticmethod
    def treats_avg_price():
        total_treats_price = treats.total_market_value / treats.total_market_volume
        return total_treats_price

#inputting the different categories that make up the treats market
choc = treats("chocolate", 6000, 1.50)
soft_drinks = treats("soft drinks", 4000, 1.90)
sweets = treats("sweets", 3000, 0.9)
crisps = treats("crisps", 2000, 1.42)

market_price = treats.treats_avg_price()
print("prints the average market price based on value and volume", market_price)
print("prints the total market volume", treats.total_market_volume)
print("prints the total market value", treats.total_market_value)



class chocolate(treats):

    chocolate_market_value = 0
    chocolate_market_volume = 0

    def __init__(self, sub_category, market_value = 0, average_price = 0.0):
        super().__init__(self, market_value, average_price)
        self.sub_category = sub_category
        self.volume = market_value / average_price
        chocolate.chocolate_market_value += market_value
        chocolate.chocolate_market_volume += self.volume

    # def __str__(self):
    #     return f'{chocolate.sub_category} has a market value of {chocolate.market_value} and an average price of {chocolate.average_price}'

    @staticmethod
    def chocolate_avg_price():
        chocolate_price = chocolate.chocolate_market_value / chocolate.chocolate_market_volume
        return chocolate_price


bar = chocolate("bars", 2000, 0.7)
blocks = chocolate("blocks", 2500, 1.45)
multipack = chocolate("multipack", 1600, 1.90)
gifting = chocolate("gifting", 200, 2.96)

print("the average price per unit for chocolate is: ", chocolate.chocolate_avg_price())
print("chocolate total market value is: ", chocolate.chocolate_market_value)
print("chocolate total market volume is: ", chocolate.chocolate_market_volume)

if choc.market_value != chocolate.chocolate_market_value:
    print("WARNING: chocolate sub categories do not add up to total category value")

class bars(chocolate):

    bars_market_value = 0
    bars_market_volume = 0

    def __init__(self, form, market_value = 0, average_price = 0.0):
        super().__init__(self, market_value, average_price)
        self.form = form
        self.volume = market_value / average_price
        bars.bars_market_value += market_value
        bars.bars_market_volume += self.volume

    # def __str__(self):
    #     return f'{bars.form} has a market value of {bars.market_value} and an average price of {bars.average_price}'

    @staticmethod
    def bars_avg_price():
        bars_price = bars.bars_market_value / bars.bars_market_volume
        return bars_price

counterlines = bars("counterlines", 1000, 0.9)
kids = bars("kidsize", 300, 0.3)
seasonal = bars("seasonal", 600, 0.7)


print("the average price per unit for bars of chocolate is: ", bars.bars_avg_price())
print("chocolate bars total market value is: ", bars.bars_market_value)
print("chocolate bars total market volume is: ", bars.bars_market_volume)

if bars.bars_market_value != bar.market_value:
    print("WARNING: bars formats do not add up to the total market value of the subcategory: bars")
