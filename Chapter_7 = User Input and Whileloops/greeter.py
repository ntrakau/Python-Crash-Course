#NT Rakau

#print(f"Hello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "#can use += operator to make multiline input prompts

name = input(prompt)
print(f"\nHello, {name.title()}!")

