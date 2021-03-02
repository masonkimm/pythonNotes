# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# constructor
numbers2 = list((1, 2, 3, 4, 5))
print(numbers, numbers2)

# to get value
print(fruits[1])

# to get length
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')

# Change a value
fruits[0] = 'Blueberries'

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Remove with pop(index)
fruits.pop(2)
print(fruits)

# Reverse the list
fruits.reverse()
print(fruits)

# Sort the list
fruits.sort()
print(fruits)

# Reverse-Sort the list
fruits.sort(reverse=True)
print(fruits)
