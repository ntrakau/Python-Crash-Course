#NT Rakau
#working with loops

magicians = ['alice', 'david', 'carolina']
#as = for every magician in the list of magicians, print the magicians name
#we created a variable magician that assign the value from magicians per loop 
for magician in magicians:
    print(magician.title() + ", that was a great trick!")#passing the result of the loop directly to a "msg"
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")