#date: 26/12/2019
#This is exercise 3.7. It reuses code from 3.4 and 3.6

#reuse from exercise 3.4
guest_list = ["prathap", "veda", "mir"]
invite = "is invited to dinner at my place"
print(f"{guest_list[0].title()} {invite}")
print(f"{guest_list[1].title()} {invite}")
print(f"{guest_list[2].title()} {invite}")

#reuse from exercise 3.6
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

#start of exercise 3.7
print("Bad news guys! I can invite only 2 people")
uninvite = "you are no longer invited for dinner at my place"
uninvite_guest = guest_list.pop()
print(f"{uninvite_guest.title()} {uninvite}")
uninvite_guest = guest_list.pop()
print(f"{uninvite_guest.title()} {uninvite}")
uninvite_guest = guest_list.pop()
print(f"{uninvite_guest.title()} {uninvite}")
uninvite_guest = guest_list.pop()
print(f"{uninvite_guest.title()} {uninvite}")
print(f"{guest_list[0].title()} {invite}")
print(f"{guest_list[1].title()} {invite}")
print("Bad news guys! No one is invited for dinner")
del guest_list[0]
del guest_list[0]
print(guest_list)
