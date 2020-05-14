#Date: 10/04/2020
#This is for exercise 6.4. List is reused from 6.3

game_genres = {
    "Max Payne" : "Action",
    "Witcher" : "Action RPG",
    "Dota 2" : "MOBA",
    "Path of Exile" : "ARPG",
    "Call of Duty" : "FPS", 
    "Hearthstone" : "Card game",
}

for game, type in game_genres.items():
    print(f"{game.title()} is of the type {type.title()}")