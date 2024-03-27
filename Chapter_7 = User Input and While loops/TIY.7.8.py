#NT Rakau

'''
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop 
through the list of sandwich orders and print a message for each order, such 
as I made your tuna sandwich. As each sandwich is made, move it to the list 
of finished sandwiches. After all the sandwiches have been made, print a 
message listing each sandwich that was made.
'''

sandwich_orders = ['tuna','peanut butter', 'chicken', 'jam']
finished_sandwiches = []

while sandwich_orders:
    s_orders = sandwich_orders.pop()

    print(f"I made your {s_orders} sandwich.")
    finished_sandwiches.append(s_orders)

for sandwich in finished_sandwiches:
    print(f"{sandwich}")

'''
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
the sandwich 'pastrami' appears in the list at least three times. Add code 
near the beginning of your program to print a message saying the deli has 
run out of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
in finished_sandwiches
'''
sandwich_orders = ['pastrami', 'pastrami', 'pastrami','tuna','peanut butter', 'chicken', 'jam']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)


'''
7-10. Dream Vacation: Write a program that polls users about their dream 
vacation. Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll
'''

vacation = {}#define the dict to be used

dream_vacation = True

while dream_vacation:
    user = input("What is your name?: ")
    prompt = input("if you could visit one place in the world, ")
    

    vacation[user] = prompt

    bye = input("\nwould you like to quit: ")
    if bye == 'no':
        dream_vacation = False


for user, prompt in vacation.items():
    print(f"\nI {user} would like to go to {prompt}")

