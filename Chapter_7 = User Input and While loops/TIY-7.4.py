#NT RAKAU

'''
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying youll add that topping to their pizza
'''
pizza_topping = "What's your pizza topping?"
pizza_topping += "\nEnter 'quit' when done: "

topping = ""
while topping != 'quit':
    topping = input(pizza_topping)
    if topping:
        print(f"Adding {topping.title()} to pizza!")

'''
7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
a persons age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15. Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket.
'''
movie = int(input("\nHow old are you? "))

if movie < 3:
    print("\nThe movie is free")
elif movie < 12:
    print("\nThe movie ticket is $10")
elif movie > 12:
    print("\nThe movie ticket is $15")


'''
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value.
'''
movie = int(input("\nHow old are you? "))


while movie:
    
    if movie < 3:
        print("\nThe movie is free")
        break
    elif movie < 12:
        print("\nThe movie ticket is $10")
        break
    elif movie > 12:
        print("\nThe movie ticket is $15")
        break
    

pizza_topping = "What's your pizza topping?"
pizza_topping += "\nEnter 'quit' when done: "

topping = ""
while topping != 'quit':
    topping = input(pizza_topping)
    if topping:
        print(f"Adding {topping.title()} to pizza!")