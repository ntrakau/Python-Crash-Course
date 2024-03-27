#NT Rakau

#positional arg for the parameter structure like 1,2
def describe_pet(animal_type, pet_name):
    """Display information abouta pet."""
    print(f"I have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
    

describe_pet('dog', 'luna')
describe_pet('hamspter', 'harry')

#keyword args== when calling the arg you associate the name-value pair
#eg describe_pet(animal_type='hamster', pet='harry')
describe_pet(animal_type='Cats',pet_name='Garfield')

#Default value
def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')