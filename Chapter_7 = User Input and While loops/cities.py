#NT Rakau

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)#declare a variable in the while statement

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")