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
    'grizzly' :{  
             'location_1':'dubai',  'cape town','new york'}, 
           
       'katixi' : {
         'location_1' : 'dubai', 
          'location_1' : 'cape town', 
          'location_1' : 'new york',
    },
    'lesiba' :{ 
          'location_1':'dubai', 
          'location_1'  :'cape town', 
          'location_1': 'new york',
    }, 
}

for names, place in favorite_places.items():
    location = place['location_1']
    print("\nHi, my name is " + names.title() + " and my favorite places are: \t")
    print("\t" + location)

  