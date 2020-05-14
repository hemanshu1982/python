#date: 10/04/2020
#this is for exercise 6.5

name_birthplace = {
    "rajesh" : "chennai",
    "ila" : "rajkot",
    "hemanshu" : "chennai",
    "dimple" : "bangalore",
    "khushi" : "bangalore",
}

for name, birthplace in name_birthplace.items():
    print(f"{name.title()} was born in {birthplace.title()}")

print("The family members are:")
for name in name_birthplace.keys():
    print(f"\t{name.title()}")

print("The different birthplaces are:")
for birthplace in set(name_birthplace.values()):
    print(f"\t{birthplace.title()}")