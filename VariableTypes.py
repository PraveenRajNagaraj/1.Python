class phone():
    chargertype="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
        print("Charger Type: ",self.chargertype)

phone.chargertype="B-Type"

samsung=phone("Samsung","1000")
samsung.display()

nokia=phone("Nokia","500")
nokia.display()
