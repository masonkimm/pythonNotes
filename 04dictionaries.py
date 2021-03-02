# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dictionary
person = {
    'first_name': 'Mason',
    'last_name': 'King',
    'age': 29
}
# print(person, type(person))
# # JS => person.first_name
# print(person['first_name'])
# print(person.get('last_name'))

# Constructor
# person2 = dict(first_name='Sara', last_name='Williams')
# print(person2, type(person2))

# Adding key/value
person['phone'] = '555-555-5555'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Washington'
print(person2)

# Remove item
del(person['age'])
person.pop('phone')

print(person)

# Clear
person.clear()
print(person)

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 52}
]

print(people)
print(people[1]['name'])
