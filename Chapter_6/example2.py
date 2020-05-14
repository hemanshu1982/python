#Date: 10/04/2020
#This is an example for Dictionary + For Loop

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'jen']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

print("\n")
for name in sorted(favorite_languages.keys()):
    print(f"Hi {name.title()}")