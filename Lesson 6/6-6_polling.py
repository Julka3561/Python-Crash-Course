favorite_languges = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
people_to_poll = [
    'jen',
    'silvester',
    'anna',
    'phil',
    'jack',
    'julia',
]
for people in people_to_poll:
    if people in favorite_languges.keys():
        print(f'{people.title()}, thank you for voting!')
    elif people not in favorite_languges.keys():
        print(f'{people.title()}, please make a vote!')