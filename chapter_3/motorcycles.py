motorcycles = ["Activa", "Honda", "Lune"]
print(motorcycles)

motorcycles[2] = "Super XL"
print(motorcycles)

motorcycles.append("Bajaj Electric")
print(motorcycles)

cars = []
cars.append("Santro")
cars.append("Nexon")
print(cars)

cars.insert(0,"Maruthi")
print(cars)

del motorcycles[3]
print(motorcycles)

print(cars)
popped_cars = cars.pop()
print(cars)
print(popped_cars)

red_car = cars.pop(1)
print(f"The only red car I have owned is {red_car}")

cars_owned = ["Martuhi", "Santo", "Nexon", "Merc"]
print(cars_owned)
cars_not_owned = "Merc"
cars_owned.remove(cars_not_owned)
print(cars_owned)
print(f"I currently dont own a {cars_not_owned}")