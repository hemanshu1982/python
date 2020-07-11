#date: 14/05/2020
#This is for exercise 6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

take_poll = ['jen','sarah','jalaja','magu']

for taken_poll in take_poll:
    if taken_poll in favorite_languages:
        print(f'Hi! {taken_poll.title()}. Thanks for taking the poll')
    else:
        print(f'Hi! {taken_poll.title()}. Please take the poll')