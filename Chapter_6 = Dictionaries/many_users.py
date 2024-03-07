#NT Rakau

#A dict inside a dict
#I can use the username as the key, and the related info as the values

users = {# a dict inside a dict
    'aeinstein' : {#username as key
        'first': 'albert',#values 
        'last': 'eistein',
        'location':'princeton',
    },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username.title())
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())