# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
  # Constructor: function that runs when you instantiate and object from a class 
  
  def __init__(self, name, age, email):
    # self => 'this'
    self.name = name
    self.age = age
    self.email = email

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1

# Init user object
brad = User('Brad Traversy', 29, 'test@gmail.com')
# print(type(brad))
# print(brad.name)
# print(brad.age)
brad.has_birthday()

print(brad.greeting())



