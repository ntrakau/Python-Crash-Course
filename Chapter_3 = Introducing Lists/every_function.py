#NT Rakau

currencies = ['euro','dollar', 'rand ', 'yen', 'shilling ', 'pound', 'naira', 'ruby', ' pula ', 'krone','peso', 'shekel','franc','antilean guilder', 'dram', 'ouguiya', ' ringgit']
#sort() method
currencies.sort()
print(currencies)
#reverse() method
currencies.reverse()
print(currencies)
#sorted()
print(sorted(currencies))
#.upper()
print(currencies[0].upper())
#.lower()
print(currencies[1].lower())
#.title()
print(currencies[2].title())
#.lstrip()
print(currencies[3].lstrip())
#.rstrip()
print(currencies[4].rstrip())
#.strip()
print(currencies[5].strip())
#len
currency = len(currencies)
print(currency)

#del
del currencies[8]
print(currencies)
#remove
currencies.remove('yen')
#fstring
print(f"The currencies I trade are {currencies[5]}, and I'm profitable")
#pop()
popped_currencies = currencies.pop(10)
print(popped_currencies)
