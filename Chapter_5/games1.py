#date: 20/01/2020
#This is example for the exercise to merge If and For statements

games = ["path of exile", "monster hunter world", "south park"]
#games = []

if games:
    for game in games:
        if game == "south park":
            print(f"Currently I am not playing the game: {game.title()}")
        else:
            print(f"Currently I am playing the game: {game.title()}")
else:
    print("I am currently not playing anying")

available_drinks = ("Beer", "Whiskey", "Rum", "Vodka", "Wine")
is_it_a_drink = ["Beer", "Milkshake", "Whiskey"]

for drink in is_it_a_drink:
    if drink in available_drinks:
        print(f"{drink} is an alcoholic drink")
    else:
        print(f"{drink} is not an alcoholic drink")
