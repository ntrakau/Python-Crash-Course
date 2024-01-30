#NT Rakau

#3.4 create a guest list containing 3 values and print messages using the list item
guest_list = ['Elon Musk', 'Dr Barbara Oakley', 'David Malan']
print("Hi, " + guest_list[0] + " you're invited to join me for dinner on Saturday.")
print("Hi, " + guest_list[1] + " you're invited to join me for dinner on Saturday.")
print("Hi, " + guest_list[2] + " you're invited to join me for dinner on Saturday.")
print("\n")

# Print a statement of the name of the person who can't make it 
print(guest_list[0])
#replace the guest who cant make it with a new guest
guest_list.remove('Elon Musk')
guest_list.append('Vusi Thembekwayo')
print(guest_list)
print("\n")

#print out messages to the new guests
print("Hi, " + guest_list[0] + " you're cordially invited to join me for dinner on Saturday.")
print("Hi, " + guest_list[1] + " you're cordially invited to join me for dinner on Saturday.")
print("Hi, " + guest_list[2] + " you're cordially invited to join me for dinner on Saturday.")
print("\n")

#bigger table found = more guest requested
print("Dear, " + guest_list[0] + " a bigger sitting arragment is aquired, so therefore more prominent indviduals will be invited to our dinner sitting.")
print("Dear, " + guest_list[1] + " a bigger sitting arragment is aquired, so therefore more prominent indviduals will be invited to our dinner sitting.")
print("Dear, " + guest_list[2] + " a bigger sitting arragment is aquired, so therefore more prominent indviduals will be invited to our dinner sitting.")
#inserting a new guest to the beginning of the list
guest_list.insert(0, "Julius Malema")
guest_list.insert(2, "Ryan Reynolds")
guest_list.append("Bobby Axelrod")
print("\n")

#Print new invitations to the guest
print("Dear, " + guest_list[0] + " you're cordially invited to dinner.")
print("Dear, " + guest_list[1] + " you're cordially invited to dinner.")
print("Dear, " + guest_list[2] + " you're cordially invited to dinner.")
print("Dear, " + guest_list[3] + " you're cordially invited to dinner.")
print("Dear, " + guest_list[4] + " you're cordially invited to dinner.")
print("Dear, " + guest_list[5] + " you're cordially invited to dinner.")
#print message "can only invite two guests"
print("I regret to inform you that, only two guest are going to be invited")
print("\n")
#popping guest out of the list
popped_guest = guest_list.pop()
print(f"Dear,{popped_guest}. Im sorry to inform you that you're popped from dinner.")
popped_guest = guest_list.pop()
print(f"Dear,{popped_guest}. Im sorry to inform you that you're popped from dinner.")
popped_guest = guest_list.pop()
print(f"Dear,{popped_guest}. Im sorry to inform you that you're popped from dinner.")
popped_guest = guest_list.pop()
print(f"Dear,{popped_guest}. Im sorry to inform you that you're popped from dinner.")
print('\n')
#informing the remaining guest of the dinner
print(f"Dear, {guest_list[0]}. I'm pleased to inform you that the dinner is still ongoing as planned.")
print(f"Dear, {guest_list[1]}. I'm pleased to inform you that the dinner is still ongoing as planned.")
print("\n")
#using len() to show the number of guests
num_guest = len(guest_list)
print(f"The number of guests for the dinner is {num_guest}.")

#del to remove the items in the list to create a empty list
del guest_list[0]
del guest_list[0]
print(guest_list)