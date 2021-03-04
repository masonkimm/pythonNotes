# # A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class

class User:
    # Constructor
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_aged(self):
        self.age += 1

# Extend class


class Customer(User):
  # Constructor
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.balace = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init customer
janet = Customer('Janet Mcconaway', 30, 'jj234@gmail.com')
janet.set_balance(500)
print(janet.greeting())
# without greeting()
# My name is Janet Mcconaway and I am 30
# with greeting()
# My name is Janet Mcconaway and I am 30 and my balance is 500

# Init user object
mason = User('Mason K', 29, 'test123csddd@gmail.com')

# print(type(mason))
# print(mason.name)
# print(mason.age)
# print(mason.email)

mason.has_aged()
# output should be +1 of original input
# print(mason.greeting())
