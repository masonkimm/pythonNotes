# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruits2 = ('Apple', )  # tuple
fruits3 = ('Apple')    # string

# Create tuple

fruits = ('Apples', 'Orages', 'Grapes')
# fruits3 = (tuple(('Apples', 'Oranges', 'Grapes')))

print(fruits, type(fruits2))
# >> ('Apples', 'Orages', 'Grapes') <class 'tuple'>

print(fruits[1])
# >> 'Oranges'

# fruits2[0] = 'Pears'
# >> typeError b/c tuples are unchangable

# to Delete tuple
# del fruits2
# print(fruits2)
# # >> not defined

# to get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# sets

fruits_set = {'Apples', 'Oranges', 'Mango'}

# check if in a set

print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Add duplicate
fruits_set.add('Apples')

# Remove from set
fruits_set.remove('Grapes')
print(fruits_set)

# clear set
fruits_set.clear()
print(fruits_set)

# delete set
del(fruits_set)
print(fruits_set)
