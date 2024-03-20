'''
7-1. Rental Car: Write a program that asks the user what kind of rental car they 
would like. Print a message about that car, such as “Let me see if I can find you 
a Subaru.”
'''
rental = input("What kind of car would you like? ")
print(f"Let me see if I can find you a {rental}.")

print("\n")

'''
7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message saying theyll have to wait for a table. Otherwise, report that their table is read
'''
restuarant = int(input("How many people are you dining with? "))

if restuarant < 8:
    print("Table is ready!")
else:
    print("You'll have to wait for a table")

print("\n")
'''
7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
number is a multiple of 10 or not
'''
multiple = int(input("Give me a number: "))

if multiple % 10 == 0:
    print(f"{multiple} is a multiple of 10!")