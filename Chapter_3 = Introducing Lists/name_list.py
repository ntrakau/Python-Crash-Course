names = ["Katixi", "Grizzly", "Lesiba", "Naruto", "Hitachi"]

#accesing individual elements/values of the list
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

#Greetings - personalised message using the list values
message = "My friend's name is"#greeting or whatever
print(message, names[0].lower() + ".")#passing the list values
print(message, names[1].upper() + ".")#in the print func to  create
print(message, names[2].title() + ".")#a personalised message
print(message, names[3].capitalize() + ".")
print(message, names[-1] + ".")

#transportation - create a list of your fave cars and print different statements about each list item
cars = ['Mercedez Benz', 'BMW one series', 'Nizzan Magnite', 'Ford Ranger']
print("My favorite car brand is " + cars[0] + ".")
print(f"This car makes me feel good {cars[1]}, first car vibes.")
print(f"Nice car, and it's affordable too. {cars[2]} also a young proffesional first car aura.")
print(f"Wa bonn {cars[-1]}, I want that big one...")