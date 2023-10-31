class dad():
    def money(self):
        print("dad's money")

class land():
    def important(self):
        print("important land")

class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s2=son2()
s2.money()


