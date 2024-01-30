#NT Rakau

#.sort()method = sort list in alphabeticall order= cannot be reversed
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
#can also sort in reverse by passing (reverse=True) as a sort arg= cannot be revesed
cars.sort(reverse=True)
print(cars)
#sorted()function - sort's the list item without changing the original list, passed in the print(sorted(cars)) fucntion as a arg
print(sorted(cars))
print(cars)

#Printing a list in reverse order
#.reverse() method ussed to reverse a list chronologically e.g a,b,c,d = d,c,b,a
#reverse() is permanent=use other method to manupilate the list
cars.reverse()
print(cars)

#finding the length of a string using the .len() method
len(cars)