class animal():
    def sound(self):
        print("Animal makes sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class bird(animal):
    def sound(self):
        print("Bird sings")

obj=dog()
obj.sound()
obj1=bird()
obj1.sound()

    
