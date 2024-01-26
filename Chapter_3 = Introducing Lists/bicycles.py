#NT Rakau
#Lists = a way to collect data in python
#a list is characterised by square brackets and the list elements are separated by a comma,
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

#to access individual elements in the list we use indexing[] to point to that particular element 
print(bicycles[0])#index 0 points to the first element in the list
print(bicycles[0].title())#str methods can be passed to lists also
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])#negative indexing used to get last item in any list

#using individual values from the list
message = "My first bicycles was a " + bicycles[0].title() + "."
print(message)
