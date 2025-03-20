dict = {}

dict['name'] = 'John'
dict['age'] = 30
dict['city'] = 'New York'

print("Dictionary:", dict)

name = dict.get('name')
age = dict.get('age')
city = dict.get('city')

print("Name:", name)
print("Age:", age)
print("City:", city)

keys = dict.keys()
print("Keys:", keys)

values = dict.values()
print("Values:", values)

non_existing_value = dict.get('country', 'Not Found')
print("Country (not in dictionary):", non_existing_value)
