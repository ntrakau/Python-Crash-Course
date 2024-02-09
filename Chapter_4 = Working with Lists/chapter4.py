#NT Rakau

#4.3 Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive
for num in range(1,21):
    print(num)

print('\n')

for one in range(1,110):
    print(one, end=' ')

print('\n')
'''
4-4. One Million: Make a list of the numbers from one to one million, and then 
use a for loop to print the numbers. (If the output is taking too long, stop it by 
pressing ctrl-C or by closing the output window.)
'''
sum_million = []
for one in range(1,101):
    sum_million.append(one)
print(sum_million)

print('\n')

'''
4-5. Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and 
ends at one million. Also, use the sum() function to see how quickly Python can 
add a million numbers.
'''
min = min(sum_million)
print(min)
max = max(sum_million)
print(max)
sum = sum(list(sum_million))
print(sum)

print('\n')

'''
4-6. Odd Numbers: Use the third argument of the range() function to make a list 
of the odd numbers from 1 to 20. Use a for loop to print each number
'''

for odd in range(1,21,3):
    print(odd,end=" ")

print('\n')

'''
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to 
print the numbers in your list.
'''
threes = []
for multiple in range(3,31):
    threes.append(multiple * 3)

print(threes)

print('\n')

'''
4-8. Cubes: A number raised to the third power is called a cube. For example, 
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
is, the cube of each integer from 1 through 10), and use a for loop to print out 
the value of each cube.
'''
cube = []
for cubes in range(1,11):
    cube.append(cubes ** 2)

print(cube)

print('\n')

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the 
#first 10 cubes
cubana = [cubanas ** 2 for cubanas in range(1,11)]
print(cubana)


