#NT Rakau

unconfirmed_users = ['alice', 'brain', 'candace']#Start with users that need to be verifieed.
confirmed_users = []# and an empty list to hold confirmed users.



while unconfirmed_users:
    current_users = unconfirmed_users.pop()#verify each user until there are no more unconfirmed users.

    print(f"Verfying user: {current_users.title()}.")
    confirmed_users.append(current_users)# move each verfied user into the list of confirmed users.


#Display all confirmed users.
print("\nTHe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())