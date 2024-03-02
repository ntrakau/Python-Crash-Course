#NT Rakau

'''
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You 
should have keys such as first_name, last_name, age, and city. Print each 
piece of information stored in your dictionary.
'''
person = {'name':'katixi','last_name': 'rakhuduwe', 'age': 30, 'city': 'Polokwane'}

print(person['name'].title())
print(person['age'])
print(person['city'].title())
print(person['last_name'].title())

'''
6-2. Favorite Numbers: Use a dictionary to store peoples favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. Print 
each persons name and their favorite number
'''
favorite_numbers = {
    'john': 5,
    'jane': 4,
    'smith': 3,
    'paul':2,
    'sarah': 1,
}

print(favorite_numbers['jane'])
print(favorite_numbers['john'])
print(favorite_numbers['paul'])
print(favorite_numbers['sarah'])
print(favorite_numbers['smith'])

#6.3 Glossary:A Python dictionary can be used to model an actual dictionary.
'''
Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values
'''
ifstatements_glossary = {
    'loops': '\n    condition ran over a argument until met\n',
    'range': '\n    range between 2 or 3 args, from but not through the first arg\n',
    'index': '\n    method of countin and or accesing items in a list/dict,start at 0\n',
    'for loop': '\n   for name in names:used to access individual chars in a list or\n',
    'if loop': '\n    runs until a particurlar condition is met',
}

print("loops" + ifstatements_glossary['for loop'].title()) 
print("range" + ifstatements_glossary['range'].title())
print("index" + ifstatements_glossary['index'].title())
print("for loop" + ifstatements_glossary['for loop'].title())
print("if loop" + ifstatements_glossary['if loop'].title())

