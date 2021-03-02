# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


## output >> 'Hi, my name is Mason and I am 29'
name = 'Mason'
age = 29

# Concatenate (str + int DNE)
print('Hi, my name is ' + name + ' and I am ' + str(age))

# ===String Formatting===

# Argument by positioning
print('Hi, my name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hi, my name is {name} and I am {age}')

# ===String Methods===
s = 'hello world'

# capitalize
print(s.capitalize())


# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
