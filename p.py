fruits = int(input("pila imong gusto nga fruits:"))
fruitsnames = []

for i in range(fruits):
    fruit = input("Enter fruit name:")
    fruitsnames.append(fruit)

print(fruitsnames)

for data in fruitsnames:
    print (data)
    if data == "Banana":
        break