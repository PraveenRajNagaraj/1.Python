class laptop():
    chargertype="C-Type"
    def __init__(self):
        self.brand=""
        self.price=35

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

    @classmethod
    def changechargertype(cls):
        cls.chargertype="B=Type"
        print("Charger Type changed to B")

    @staticmethod
    def info():
        print("This is laptop class")

hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechargertype()

hp.info()

