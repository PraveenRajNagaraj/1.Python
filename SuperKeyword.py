class a():
    def __init__(self):
        print("A")
        
    def display(self):
        print("You are in Class A")

class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("You are in Class B")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("You are in Class C")

obj=c()
 
