class myClass():

    __privateVar = 0


    def __privateMethod(self):
        print("I'm in class myClass")

    def hello(self):
        print("Private Variable value:",myClass.__privateVar)

        myClass.__privateMethod(self)  # Accessing the private method within the class

foo = myClass()
foo.hello()
