#date: 27/12/2019
#This is an example

for value in range(1,6):
    print(value)

numbers = list(range(6))
print(numbers)

even_numbers = list(range(2,200,2))
print(even_numbers)

squares = []
for value in range (1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)