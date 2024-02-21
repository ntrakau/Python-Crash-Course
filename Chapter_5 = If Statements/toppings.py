#NT Rakau

requested_toppings = 'mushrooms'

#checking for inequalities
if requested_toppings != "anchovies":
    print("Hold the anchovies!")


print("\n")

#Testing for Multiple conditions
#the if-elif-else test for one condition and when that condition is met
#python skips over all the other code blocks
#To co
requested_toppings = ['mushrooms','green peppers', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

print('\n')

#But what if the pizzeria runs out of green peppers? An if statement 
#inside the for loop can handle this situation appropriately:
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want plain pizza?")

print("\nMartell ke star")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni','extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + '.' )
print("\nFinished making your pizza!")
