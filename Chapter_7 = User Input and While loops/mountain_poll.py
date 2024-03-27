#NT Rakau

responses = {}

#set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    #store the response in the dict
    responses[name] = response

    #find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False


#polling is complete. show the results.
print("/n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


'''
The program first defines an empty dictionary (responses) and sets a flag 
(polling_active) to indicate that polling is active. As long as polling_active is 
True, Python will run the code in the while loop. 
Within the loop, the user is prompted to enter their username and a 
mountain theyd like to climb u. That information is stored in the responses
dictionary v, and the user is asked whether or not to keep the poll running w. If they enter yes, the program enters the while loop again. If they 
enter no, the polling_active flag is set to False, the while loop stops running, 
and the final code block at x displays the results of the poll
'''