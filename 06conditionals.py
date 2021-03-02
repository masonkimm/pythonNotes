## If/ Else conditions are used to decide to do something based on something being true or false

x = 3
y = 11

## Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# if x > y:
#     print(f'x:{x} is greater than y:{y}')
# elif x == y:
#     print(f'x:{x} is equal to y:{y}')
# else:
#     print(f'x:{x} is not greater than y:{y}')

# Nested if
# if x > 2:
# 	if x <= 10:
# 		print(f"x:{x} is greater than 2 but less than or equal to 10")


## Logical operators (and, or, not) - Used to combine conditional statements

# # and
# if x > 2 and x <= 10:
# 	print(f"x:{x} is greater than 2 but less than or equal to 10")
# # or
# if x > 2 or x < 3:
# 	print(f"x:{x} is greater than 2 or x: {x} is less than 10")
# # not
# if not(x == y):
# 	print(f'x:{x} is not equal to y:{y}')


## Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1, 2, 3, 4, 5]

# if x in numbers:
# 	print(x in numbers)
# 	# >> True

# if y not in numbers:
# 	print(y not in numbers)
# 	# >> True

## Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
	print (x is y)