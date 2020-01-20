#date: 26/12/2019
#This is exercise 3.6. Code from exercise 3.4

#reuse from exercise 3.4
guest_list = ["prathap", "veda", "mir"]
invite = "is invited to dinner at my place"
print(f"{guest_list[0].title()} {invite}")
print(f"{guest_list[1].title()} {invite}")
print(f"{guest_list[2].title()} {invite}")

#start of exercise 3.6
print("Great news guys i can invite more people")
guest_list.insert(0,"Ragha")
guest_list.insert(3,"Vivek")
guest_list.append("Pradeep")
print(f"{guest_list[0].title()} {invite}")
print(f"{guest_list[1].title()} {invite}")
print(f"{guest_list[2].title()} {invite}")
print(f"{guest_list[3].title()} {invite}")
print(f"{guest_list[4].title()} {invite}")
print(f"{guest_list[5].title()} {invite}")