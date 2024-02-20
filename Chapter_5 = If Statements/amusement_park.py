#NT Rakau

#if-elif-else chain
'''
Python executes only one 
block in an if-elif-else chain. It runs each conditional test in order until 
one passes. When a test passes, the code following that test is executed and 
Python skips the rest of the tests
'''
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age = 50

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")