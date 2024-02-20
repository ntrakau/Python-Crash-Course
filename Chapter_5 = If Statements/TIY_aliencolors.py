#NT Rakau
'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
'''

#Alien Color \#1
alien_color = "yellow"

#Write an if statement to test whether the alien’s color is green. If it is, print 
#a message that the player just earned 5 points
if alien_color == "green":
    print("\nPlayer earned 5 points!!")

#Write one version of this program that passes the if test and another that 
#fails. (The version that fails will have no output.)
if alien_color == "yellow":
    print("\nPlayer has earned 5 points!!!")
elif alien_color == "red":
    print("\nPlayer has not earned points!!")

#5.4 Alien Colors #2:choose a color as in 5.3 and write an if-esle chain
alien_color2 = "red"

#If the alien’s color is green, print a statement that the player just earned 
#5 points for shooting the alien.

if alien_color2 == "green":
    print("\nPlayer just earned 5 points.!!")
else:
    print("\nPlayer just earned 10 points.!!")

#Write one version of this program that runs the if block and another that 
#runs the else block.


alien_colors = "green"

if alien_colors == alien_colors:
    print("\nPlayer just earned 5 points!!")
else:
    print("\nPlayer just earned 10 points!!") 

#5.5 Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-esle chain.

if alien_colors == "green":
    print("\nPlayer earned 5 points")
elif alien_colors == "yellow":
    print("\nPlayer just earned 10 points")
elif alien_colors == "red":
    print("\nPlayer just earned 15 points")

#5.6 Stages of Life: Write an if-elif=else chain that determines a person's stage of life. Set a value for the variable age and then:
    
age = -2

if age < 2:
    print("You're a baby!")
elif age <4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're a adult!")
else:
    print("You're an elder!")


#5.7 Favorite fruit: Make a list of your favorite, and then write a series of independent if statements that check for certain fruits in your list

favorite_fruits = ['mango', 'litchi', 'lemon', 'watermelon', 'avocado']

if 'mango' in favorite_fruits:
    print("\nYour really like Mangoes.")

if 'litchi' in favorite_fruits:
    print("\nYou must eat more litchis.")
    
if 'lemon' in favorite_fruits:
    print("\nYou're eating too much lemon's.")

if 'watermelon' in favorite_fruits:
    print("\nYou must eat more watermelon.")

if 'avocado' in favorite_fruits:
    print("\nYou must eat more avos.")

 