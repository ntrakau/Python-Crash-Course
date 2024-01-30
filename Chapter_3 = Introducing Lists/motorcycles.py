#NT Rakau
#a list of motorcycles
motorcycles = ['Honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'#modifyng a list or replacing a list item,you target the index in the variable and assign a value
print(motorcycles)

#append - a str method that add elements to the end of the list
motorcycles.append('ducati')
print(motorcycles)

#using .append method to pass in values dynamically to a list
motorcycles = []#1st create a empty list
motorcycles.append('Big boy')#append values to that list
motorcycles.append('BMW')
motorcycles.append('thuthuthu')
print(motorcycles)

'''
INSERT - pass in a value at any position in a list by passing the index and value = insert(0,value)- insert takes two arguments - an int and a value (str/int)
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "Harly Davidson")#adding harley to the string at 1st
print(motorcycles)

#Removing Items from a list
#If you know the position of the item you want to remove from a list = USE THE del statement
del motorcycles[0]
del motorcycles[1]
print(motorcycles)

#Removing an item using the .pop()
#.pop() returns the removed value = it removes the last item in a list
popped_motorcycle = motorcycles.pop()#assign a variable to catch the popped item
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['Honda', 'yamaha', 'suzuki']
print(motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#also .pop() method can be used to remove an item from anywhere in the list, using the index[]
motorcycles = ['Honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + '.')

#Removing an item by value
#.remove() used to remove items from list by value if position of the item is not known
motorcycles = ['Honda', 'yamaha', 'yamaha','suzuki', 'ducati']
motorcycles.remove("yamaha")
print(motorcycles)

#just like pop() , you can work on the item removed by remove()
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
