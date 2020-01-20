#date: 20/01/2020
#This is for exercise 5.10

current_passwords = ["Passw0rd456", "Passw0rd$", "Passw0rd!@#"]
new_passwords = ["Passw0rd456", "PASSW0RD$", "Password890"]
lower_current_passwords = []

for current_password in current_passwords:
    lower_current_passwords.append(current_password.lower())

for new_password in new_passwords:
    if new_password.lower() in lower_current_passwords:
        print("Password has been used before")
    else:
        print("Password is accepted")