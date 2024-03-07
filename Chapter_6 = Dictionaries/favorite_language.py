#NT Rakau
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")#favorite_languages['sarah'] calls the value to print 

#looping through a dict
name, languagfor e in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

#using the key() method to print out only the keys from the dict.
    
for name in favorite_languages.keys():
    print(name.title())
#same as using a key() method 
for name in favorite_languages:
    print(name.title())

#accessing keys in a dict to pass a message to
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

#checking to see if a key is in the dict
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

#getting the output in order we user the sorted(), return the output in alphabetic order
for name in sorted(favorite_languages.keys()):#sort the dict first before printing the results of the for loop.
    print(name.title() + ", thank you for taking the poll.")

#printing out values without the keys we use .value()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#printing our values once, and not repeating output we use set() function
    
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages: 
        print("\t" + language.title())

