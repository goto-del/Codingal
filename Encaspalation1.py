class Computer():

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price:", self.__maxprice)

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000  # This will not change the max price
c.sell()  # Still shows the original max price

c.setMaxPrice(1000)  # This will change the max price
c.sell()  # Now shows the updated max price