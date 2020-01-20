#date: 20/01/2020
#This is for exercise 5.8

users = ["Khushi", "Ila", "Dimple", "Rajesh", "Hemanshu"]

for user in users:
    if user == "Hemanshu":
        print(f"Welcome {user}. You will be logged in as admin")
    else:
        print(f"Welcome {user}. You will be logged in as a regular user")