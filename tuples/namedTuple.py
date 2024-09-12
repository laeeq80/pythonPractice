from collections import namedtuple

# Creating a namedtuple type
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating an instance of the namedtuple
person = Person(name="John", age=30, city="New York")

# Accessing fields by name
print(person.name)  # Output: John
print(person.age)   # Output: 30
print(person.city)  # Output: New York
