#NT Rakau

user_o = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

'''
Creating a for loop for a dict you pass in variables that will be assigned the key and value values.
e.g key = assign a variable that will catch the key value in print
pass .item() method to list out items in the dict and pass them to the specified variables
'''
for key,value in user_o.items():#for loop for a dict
    print("\nKey: " + key)
    print("\nValue: " + value)

