#date: 27/12/2019
#This is for exercise 4.12. I will reuse code from 4.11

my_foods = ["Pizza", "Pasta", "Burgers", "Idli Vada"]
khushi_foods = my_foods[:]

my_foods.append("Biryani")
khushi_foods.append("Roti Sabzi")

print("My favourite foods are:")
for my_food in my_foods:
    print(my_food)
print("Khushi's favourite foods are:")
for khushi_food in khushi_foods:
    print(khushi_food)