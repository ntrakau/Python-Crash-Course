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
