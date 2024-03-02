#NT Rakau

alien_0 = {'color': 'green', 'points': 5}#{}curly braces to used dict= we pass and object and value

print(alien_0['color'])
print(alien_0['points'])

#calling the dict values
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!") 
print("You just earned " + str(alien_0['points']) + " points!")

#Adding new values to the dict.
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#dict are mutable 
#Modifying values in a dict
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0 = {'color': 'yellow'} 
print("The alien is now " + alien_0['color'] + ".")


Martell = {}#started with an empty dict.

Martell['Name'] = 'Martell' #passed keys and they're values
Martell['Occupation'] = 'Cloud Engineer'
Martell['Age'] = 32

print("His name is " + Martell['Name'] + " and he works as a " + Martell['Occupation'] + " he is " + str(Martell['Age']) + " years old, very very handsome!!!") #printed out a text using dict
print(Martell)

#Removing Key-Values Pairs
#Be aware that the deleted key-value pair is removed permanently.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']#del requires name of dict and key 
print(alien_0)


