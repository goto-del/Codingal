class Computer:

    def __init__(self):
        self.__maxprice = 9000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxprice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.setMaxprice(10000)
c.sell()