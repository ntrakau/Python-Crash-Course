In this chapter you’ll learn how to use 
Python’s dictionaries, which allow you to 
connect pieces of related information. You’ll 
learn how to access the information once it’s 
in a dictionary and how to modify that information. 
Because dictionaries can store an almost limitless 
amount of information, I’ll show you how to loop through the data in a 
dictionary. Additionally, you’ll learn to nest dictionaries inside lists, lists 
inside dictionaries, and even dictionaries inside other dictionaries.
Understanding dictionaries allows you to model a variety of real-world 
objects more accurately. You’ll be able to create a dictionary representing a 
person and then store as much information as you want about that person. 
You can store their name, age, location, profession, and any other aspect of 
a person you can describe. You’ll be able to store any two kinds of information that can be matched up, such as a list of words and their meanings, a 
list of people’s names and their favorite numbers, a list of mountains and 
their elevations, and so forth.

Working with Dictionaries
A dictionary in Python is a collection of key-value pairs. Each key is connected 
to a value, and you can use a key to access the value associated with that key. 
A key’s value can be a number, a string, a list, or even another dictionary. 
In fact, you can use any object that you can create in Python as a value in a 
dictionary.
In Python, a dictionary is wrapped in braces, {}, with a series of keyvalue pairs inside the braces, as shown in the earlier example:
alien_0 = {'color': 'green', 'points': 5}
A key-value pair is a set of values associated with each other. When you 
provide a key, Python returns the value associated with that key. Every key 
is connected to its value by a colon, and individual key-value pairs are separated by commas. You can store as many key-value pairs as you want in a 
dictionary.
The simplest dictionary has exactly one key-value pair, as shown in this 
modified version of the alien_0 dictionary:
alien_0 = {'color': 'green'}
This dictionary stores one piece of information about alien_0, namely 
the alien’s color. The string 'color' is a key in this dictionary, and its associated value is 'green'.