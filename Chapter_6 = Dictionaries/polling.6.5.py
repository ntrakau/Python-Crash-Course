#NT Rakau

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['erin', 'john', 'sarah', 'phil']
for person in people:
    if person not in favorite_language.keys():
        print(person.title() + ", please take the poll!".title())
for name in favorite_language.keys():
    print(name.title() + " thank you for your participation!".title())