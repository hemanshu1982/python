#date: 26/12/2019
#This is exercise 3.5. Code from exercise 3.4 is reused

#reuse from exercise 3.4
guest_list = ["prathap", "veda", "mir"]
invite = "is invited to dinner at my place"
print(f"{guest_list[0].title()} {invite}")
print(f"{guest_list[1].title()} {invite}")
print(f"{guest_list[2].title()} {invite}")

#start of exercise 3.5
print(f"{guest_list[1].title()} cant make it for dinner at my place")

del guest_list[1]
guest_list.append("Vivek")
print(f"{guest_list[0].title()} {invite}")
print(f"{guest_list[1].title()} {invite}")
print(f"{guest_list[2].title()} {invite}")
