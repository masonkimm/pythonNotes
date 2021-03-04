# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"firstName": "Wade", "lastName": "Doe", "age": 30 }'

# Parse to dictionary

user = json.loads(userJSON)
# print(user)

# print(user['firstName'])
# Wade


# Dictionary => JSON

car = {'make': 'Ford', 'model': 'Mustant', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)
