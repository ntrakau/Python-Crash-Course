#NT Rakau

'''
6-5. Rivers: Make a dictionary containing three major rivers and the country 
each river runs through. One key-value pair might be 'nile': 'egypt'.
'''

rivers = {
    'nile' : 'egypt',
    'amazon': 'brazil',
    'vaal': 'south africa'
}

#Use a loop to print a sentence about each river, such as The Nile runs 
#through Egypt.
for river, message in rivers.items():
    print("The " + river.title() + " run's through " + message + ".")

#Use a loop to print the name of each river included in the dictionary
for river_name in rivers.keys():
    print(river_name.title())

# Use a loop to print the name of each country included in the dictionary.
for country_name in rivers.values():
    print(country_name.title())