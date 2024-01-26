Naming and Using Variables

When you’re using variables in Python, you need to adhere to a few rules and guidelines. Breaking some of these rules will cause errors; other guidelines just help you write code that’s easier to read and understand. Be sure to keep the following variable rules in mind:

•	 Variable names can contain only letters, numbers, and underscores. 
They can start with a letter or an underscore, but not with a number. 
For instance, you can call a variable message_1 but not 1_message.
•	 Spaces are not allowed in variable names, but underscores can be used 
to separate words in variable names. For example, greeting_message works, 
but greeting message will cause errors.
•	 Avoid using Python keywords and function names as variable names; 
that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print. (See “Python Keywords 
and Built-in Functions” on page 489.)
•	 Variable names should be short but descriptive. For example, name is 
better than n, student_name is better than s_n, and name_length is better 
than length_of_persons_name.
•	 Be careful when using the lowercase letter l and the uppercase letter O
because they could be confused with the numbers 1 and 0

Strings

A string is simply a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this: 

"This is a string."
'This is also a string.'

This flexibility allows you to use quotes and apostrophes within your strings:

'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

#to implement changes done to a variable we store the variable back into the variable e.g name = "martell" name = name.title() name = "Martell"