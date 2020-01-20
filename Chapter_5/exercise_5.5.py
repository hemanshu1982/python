#date: 30/12/2019
#This is for exercise 5.5. Code from 5.3 is copied as exercise is completed

alien_colour = "yellow"

if alien_colour == "green":
    points = 10
elif alien_colour == "yellow":
    points = 20
elif alien_colour == "red":
    points = 30
else:
    points = 0

print(f"Congrats! You have scored {points} points ")
