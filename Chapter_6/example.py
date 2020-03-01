#date: 20/01/2020
#This is an example for disctionaries

alien_0 = {"colour": "Green", "points": 5}
print(alien_0["colour"])
print(alien_0["points"])

alien_0["x_axis"] = 0
alien_0["y_axis"] = 25

print(alien_0)

alien_0["speed"] = "medium"

print(alien_0)

if alien_0["speed"] == "slow":
    increment = 1
elif alien_0["speed"] == "medium":
    increment = 2
else:
    increment = 3

alien_0["x_axis"] = alien_0["x_axis"] + increment

print(alien_0)

del alien_0["speed"]

print(alien_0)

speed_1 = alien_0.get("Speed", "No Speed assigned")
print(speed_1)