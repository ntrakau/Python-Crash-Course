#NT Rakau
#Slicing a list = to slice a list you perfom an index of where you want to slice e.g slice[2:4]
#slice takes two index args to work with

players = ['charles','martina','michael','florence','eli']
print(players[0:3])

#create a subset of list
print(players[1:4])

#slicing a list from the first element, the is no need to specify the first index e.g players[:4]
print(players[:2])

#slicing to the end of the list
print(players[2:])

#slicing from the end of the list use the negative - e.g players[-3:]
print(players[-3:])

#looping through players
print("Here's are the first three players on my team:")
for player in players[:3]:
    print(player.title())