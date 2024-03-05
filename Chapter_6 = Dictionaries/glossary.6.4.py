#NT Rakau

#6.4 Glossary2:A Python dictionary can be used to model an actual dictionary.
'''
Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values
'''
ifstatements_glossary = {
    'loops': 'condition ran over a argument until met',
    'range': 'range between 2 or 3 args, from but not through the first arg',
    'index': 'method of countin and or accesing items in a list/dict,start at 0',
    'for loop': 'for name in names:used to access individual chars in a list or',
    'if loop': 'runs until a particurlar condition is met',
}
'''
print("loops" + ifstatements_glossary['for loop'].title()) 
print("range" + ifstatements_glossary['range'].title())
print("index" + ifstatements_glossary['index'].title())
print("for loop" + ifstatements_glossary['for loop'].title())
print("if loop" + ifstatements_glossary['if loop'].title())
'''
for glossary, meaning in ifstatements_glossary.items():
    print('\n' + glossary.title())
    print(meaning.title())