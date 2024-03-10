#NT Rakau


'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person.

'''
people_0 = {'name':'katixi',
            'last_name': 'rakhuduwe',
            'age': 30, 
            'city': 'Polokwane'
}
people_1 = {
    'name': 'manamela',
    'last_name': 'lesiba',
    'age': 33,
    'city': 'manchester',
}
people_2 = {
    'name': 'grizzly',
    'last_name': 'gafane',
    'age': 30,
    'city': 'dubai'
}

people = [people_0, people_1, people_2]

for person in people:
    for name, value in person.items():
        print(name.title())
        print("\tInformation: " + str(value))

'''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet. In each dictionary, include the kind of animal and the owner’s 
name. Store these dictionaries in a list called pets. Next, loop through your list 
and as you do print everything you know about each pet.
'''
kitty = {
    'type': 'cat',
    'owner': 'sandra',
}
luna = {
    'type': 'dog',
    'owner': 'sarah',
}
goldi = {
     'type': 'fish',
    'owner': 'timmy'
   
}
pets = [kitty,luna,goldi]

for pet in pets: 
    for animal,info in pet.items():
        print(animal.title() + ":" + "\t" + info.title())

'''
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person. To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places. Loop through the dictionary, and print 
each person’s name and their favorite places
'''
favorite_places = {
    'grizzly' : ['dubai', 'new york', 'spain'],
    'katixi' : ['brazil', 'china', 'mauritaus'],
    'lesiba' : ['cape town', 'afghanistan', 'cuba'],
}

for name,places in favorite_places.items():
    print(f"Hi, my name is {name.title()}. And my favorite places are:")
    for value in places:
        print(f"\t{value.title()}")
  
'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
each person can have more than one favorite number. Then print each person’s 
name along with their favorite numbers
'''
favorite_numbers = {
    'john': [5,6,7],
    'jane': [4,3,2],
    'smith': [3,76],
    'paul':[2,9],
    'sarah': [1,2,3],
}

for name,value in favorite_numbers.items():
    print(f"Hi, my name is {name.title()}, and my lucky numbers are: ")
    for values in value:
        print(f"\t{values}")

'''
6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
keys in your dictionary. Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the information you have stored about it
'''
cities = {
    'polokwane' : {
        'country': 'south africa',
        'population': 493951,
        'fact': 'polokwane means place of safety',
        },

    'tokyo' : {
        'country': 'japan',
        'population': 14000000,
        'fact': 'worlds largest city',
        },
    
    'new york' : {
        'country': 'united states',
        'population': 8500000,
        'fact': 'new York is often called the big city',
        },

    }
for k, v in cities.items():
    print(f"Country: {k.title()}")

    about_country = v['population']
    fact = v['fact']

    print(f"\tPopulation: {str(about_country)}")
    print(f"\tFact: {fact.title()}")

'''
6-12. Extensions: We’re now working with examples that are complex enough 
that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.
'''

