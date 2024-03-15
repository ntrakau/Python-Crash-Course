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