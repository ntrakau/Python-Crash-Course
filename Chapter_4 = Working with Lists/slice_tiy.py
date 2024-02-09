#NT Rakau
#chapter 4 = slicing = TRY IT YOURSELF

players = ['charles','martina','michael','florence','eli', 'ronaldo', 'messi', 'mbappe', 'neymar']

print("The first three players in the list are:")
for player in players[:3]:
    print(player.title())

print("\nThree items from the middle of the list are:")
for player in players[3:6]:
    print(player.title())

print("\nThe last three players in the list are:")
for player in players[-3:]:
    print(player.title())

'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
'''
pizzas = ['chicken', 'beef', 'hawain']
friends_pizzas = pizzas[:]

#Add a new pizza to the original list
pizzas.append('meatty')
#Add a different pizza to the list friend_pizzas.
friends_pizzas.append('cheese crust')


print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)

print("\n")

'''
4-12. More Loops: All versions of foods.py in this section have avoided using 
for loops when printing to save space. Choose a version of foods.py, and 
write two for loops to print each list of foods.
'''
my_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
for food in my_food:
    print(food)

print('\n')
my_friends_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
for food in my_friends_food:
    print(food)



