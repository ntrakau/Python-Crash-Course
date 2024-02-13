#NT Rakau

'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
describing each test and your prediction for the results of each test. Your code 
should look something like this
'''
name = "Martell"

print("Is name == 'Martell'? I predict true")
print(name == "Martell")

print("Is name == 'Joseph'? I predict False")
print(name == "Joseph")

ice_cream = "vanilla"

print("\nIs ice cream == 'vanilla'? I predict True")
print(ice_cream == "vanilla")
print("Is ice cream == 'chocolate'? I predict False")
print(ice_cream == "chocolate")

shoe_size = 7

print('\nshoe size == 7, I predict True')
print(shoe_size == 8)
print("Is shoe_size == 9? I predict False")
print(shoe_size == 9)

shirt = "white"

print("\nIs my shirt != white? I predict False")
print(shirt != "white")
print("Is my shirt not equal to white")
print(shirt != "white")

price_of_coffee = float(10.00)
print("\nIs the price of coffee R10.00? I predict True")
print(price_of_coffee == 10.00)
print("The price of coffee is 12.00, I predict False")
print(price_of_coffee == 12.00)

print('\n')
'''
5-2. More Conditional Tests: You don't have to limit the number of tests you 
create to 10. If you want to try more comparisons, write more tests and add 
them to conditional_tests.py. Have at least one True and one False result for 
each of the following:
'''

#Tests for equality and inequality with strings
car = "Mercedez Bens"
print(car == "Mercedez Bens")
print(car == "BMW")

print('\n')

#Tests using the lower() function
print(car.lower() == "mercedez bens")
print(car)

print('\n')

#Numerical tests involving equality and inequality, greater than and 
#less than, greater than or equal to, and less than or equal to
four = 4
print(four == 5)#equality opt
print(four != 4)#unequality
print(four > 10)#greater than
print(four < 10)#less than
print(four >= 10)#greater of equal to
print(four <= 10)#less of equal to

print('\n')
#Tests using the and keyword and the or keyword
print((four > 10) and (four < 10))
print((four == 4) or (4 != four))

numbers = [1,2,3,4,5,6,7,8]
print( 3 in numbers)#Test whether an item is in a list
print( 3 in numbers)#
print( 9 not in numbers)#Test whether an item is not in a list

