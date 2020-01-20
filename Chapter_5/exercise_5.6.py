#date: 30/12/2019
#This is for exercise 5.6

age = 67

if age <= 2:
    type = "baby"
elif age <= 4:
    type = "toddler"
elif age <= 13:
    type = "kid"
elif age <= 20:
    type = "teenager"
elif age <= 65:
    type = "adult"
else:
    type = "elder"

print(f"You are of the type: {type}")