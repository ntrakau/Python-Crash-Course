#NT Rakau


'''
5-8. Hello Admin: Make a list of five or more usernames, including the name 
'admin'. Imagine you are writing code that will print a greeting to each user 
after they log in to a website. Loop through the list, and print a greeting to 
each user:
'''
hello_admin = ['admin', 'john', 'jane', 'smith', 'azubi']

for users in hello_admin:
    if users == 'admin':
        print("\nHello " + users + ", would you like to see a status report?\n")
    else:
        print("Hello " + users + ", thank you for logging in again.")

#5.9 No Users: Add an if test to hello_admin to make sure the list of users is not empty
hello_admin = []

if hello_admin == 'admin':
    print("Hello user")
else:
    print('We need to find more users')

#5-10. Checking Usernames: Do the following to create a program that simulates 
#how websites ensure that everyone has a unique username.
print("5.10")
current_users = ['john', 'jane', 'smith', 'doe', 'peter']

new_users = ['john', 'jane', 'allen', 'sussy']

for user in new_users:
    if user in current_users:
         print( user + " is not available, choose another username!.")
    else:
        print("Username " + user + " is available!")

#5.11 Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1,2,3.
print('\n5.11')
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
     if number == 1:
         print(str(number) + "st")
     elif number == 2:
         print(str(number)+ "nd")
     elif number == 3:
         print(str(number) + "rd")
     else:
         print(f"{number}th")
