#NT Rakau

#finding the square root of intergers using the range() and for loops
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

squares = []
for value in range(1,20):
    squares.append(value**2)

print(sum(squares))
print(max(squares))
print(min(squares))