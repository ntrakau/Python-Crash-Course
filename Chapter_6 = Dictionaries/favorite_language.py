#NT Rakau
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_language['sarah'].title() + ".")#favorite_language['sarah'] calls the value to print 

#looping through a dict
for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

#using the key() method to print out only the keys from the dict.
    
for name in favorite_language.keys():
    print(name.title())
#same as using a key() method 
for name in favorite_language:
    print(name.title())

#accessing keys in a dict to pass a message to
friends = ['phil','sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_language[name].title() + "!")

#checking to see if a key is in the dict
if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll")

#getting the output in order we user the sorted(), return the output in alphabetic order
for name in sorted(favorite_language.keys()):#sort the dict first before printing the results of the for loop.
    print(name.title() + ", thank you for taking the poll.")

#printing out values without the keys we use .value()
print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

#printing our values once, and not repeating output we use set() function
    
print("The following languages have been mentioned:")
for language in set(favorite_language.values()):
    print(language.title())