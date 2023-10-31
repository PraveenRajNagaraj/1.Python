f=open("Fruits.txt","a")
f.write("\nOrange\n")
f.write("Grapes")
f.close()

f=open("Fruits.txt","r+")
print(f.readline()) 
