class laptop:
    price=0
    processor=""
    ram=""

HP = laptop()
DELL = laptop()
LENOVO = laptop()

HP.price="1200$"
DELL.price="1300$"
LENOVO.price="7800$"

HP.processor="ABC"
DELL.processor="DEF"
LENOVO.processor="GHI"


HP.ram="200GB"
DELL.ram="300GB"
LENOVO.ram="500GB"

print(HP.price, HP.processor, HP.ram)
print(DELL.price, DELL.processor, DELL.ram)
print(LENOVO.price, LENOVO.processor, LENOVO.ram)
