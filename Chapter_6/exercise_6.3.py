#date: 01/03
#This is for exercise 6.3 Replaced coding languages with games

game_genres = {
    "Max Payne" : "Action",
    "Witcher" : "Action RPG",
    "Dota 2" : "MOBA"
}

print(f"Max Payne is an {game_genres['Max Payne']} game\n")
print(f"Witcher is an {game_genres['Witcher']} game\n")
print(f"Dota 2 is an {game_genres['Dota 2']} game\n")

#Advanced topic?
for game, game_genre in game_genres.items():
    print(f"{game} is an {game_genre}")