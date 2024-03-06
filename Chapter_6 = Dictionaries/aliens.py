#NT RAKAU

#Nesting of dict's 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]#nesting by putting the dicts inside a list

for alien in aliens:
    print(alien)


#Making an empty list for storing aliens.
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5,'speed': 'slow'}
    aliens.append(new_alien)

#Changing the state of the first 3 alien in the 
for alien in aliens[0:3]:#slice and loop through the first 3 aliens
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Show the first 5 aliens
for alien in aliens[:5]:#we use a slice to print the first five aliens
    print(alien)
print("...")

#Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

