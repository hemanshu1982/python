#date:28/12/2019
#This is an example for if statements. Replacing cars with games

games = ["Gears 4", "Gears 5", "Southpark"]
for game in games:
    if game == "Southpark":
        print(f"I am currently playing {game}")
    else:
        print(f"I have completed playing {game}")

pizza_topping = "onion"

if pizza_topping != "pineapple":
    print("hold the pineapple")

banned_users = ["Khushi", "Dimple", "Hemanshu"]
user = "Ila"

if user not in banned_users:
    print(f"{user} you can go ahead and make a post")