class company():
    def __init__(self):
        self._companyname="Google"

class b(company):
    pass

obj=b()
print(obj._companyname)
