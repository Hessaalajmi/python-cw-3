# write your code here
favorite_animals = ['dog', 'cat', 'rabbit', 'monkey']
print(favorite_animals)
print(favorite_animals[2])
favorite_animals.remove('monkey')
favorite_animals.append('fish')

for oneAnimal in favorite_animals:
    print(f'I love {oneAnimal}' )

numbers = [1, 2 , 3, 4 , 5]
numbers_sum = 0

for oneNumber in numbers:
    numbers_sum = oneNumber + numbers_sum
print(numbers_sum)
