#NT Rakau

'''
7-1. Rental Car: Write a program that asks the user what kind of rental car they 
would like. Print a message about that car, such as “Let me see if I can find you 
a Subaru.”
'''

rental = input("What car would you like to rent today? ")

print(f"\nOk, thanks for choosing {rental}. Let's go get it.")

'''
7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
'''
dinner = input("How many people are dining with you? ")
dinner = int(dinner)
if dinner >= 8:
    print("\nI'm sorry, you'll have to wait for a table")
else:
    print("\nYou're table is ready")

'''
7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
number is a multiple of 10 or not.
'''
multiple = input("Enter a number, and I'll tell you if it's a multiple of ten: ")
multiple = int(multiple)

if multiple % 10 == 0:
    print(f"\n{multiple} is a multiple of ten!")
else:
    print(f"\n{multiple} is not a multiple of ten!")