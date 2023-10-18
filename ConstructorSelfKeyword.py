class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("Processor:",self.processor)

HP=laptop()
dell=laptop()

HP.ram="8GB"
HP.processor="i5"

dell.ram="16GB"
dell.processor="i7"

HP.display()
dell.display()
