#store key:value (hash table)



# Creating a dictionary
#key must be unique
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

# Modifying values
my_dict["age"] = 31

# Adding a new key-value pair
my_dict["gender"] = "Male"

# Removing a key-value pair
del my_dict["city"]

# Checking if a key is in the dictionary
if "city" in my_dict:
    print("City:", my_dict["city"])  # This won't be executed because "city" is no longer in the dictionary

# Iterating through keys and values
for key, value in my_dict.items():
    print(key, ":", value)
