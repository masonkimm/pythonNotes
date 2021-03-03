# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Mason', 'Afton', 'Emma', 'Susan']

# simple for loop

# for person in people:
#   print(f'Current person: {person}')

## break
# for person in people:
#   if person == 'Emma':
#     break
#   print(f'Current person: {person}')
# >> mason, afton

## continue
# for person in people:
#   if person == 'Afton':
#     continue
#   print(f'Current person: {person}')
# # >> mason, emma, susan

## range
# for i in range(len(people)):
#   print(people[i])

# for i in range(0, 11):
#   print(f'number: {i}')


## While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
  print (f'Count: {count}')
  count += 1
  