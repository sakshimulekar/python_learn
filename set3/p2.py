# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

# Initialize an empty dictionary
person_dict = {}

# Function to add a new name-age pair
def add_name_age(name, age):
    person_dict[name] = age

# Function to update the age of a name
def update_age(name, new_age):
    if name in person_dict:
        person_dict[name] = new_age

# Function to delete a name from the dictionary
def delete_name(name):
    if name in person_dict:
        del person_dict[name]

# Test the functions
add_name_age("John", 25)
print(person_dict)

update_age("John", 26)
print(person_dict)

delete_name("John")
print(person_dict)
