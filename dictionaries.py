# Dictionary: key-value pair, unordered, mutable
my_dict = {**dict1, **dict2}  # merging dictionaries into my_dict

my_dict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

my_dict = dict(
    name="Max",
    age=28,
    city="New York"
)

# add an element
my_dict["element"] = "element_value"
my_dict["thing"] = "jjjj"
my_dict["ggint"] = "oooooooo"

# override an element
my_dict["element"] = "another_element_val"

# delete items
del my_dict["element"]
my_dict.pop("age")

# check if key-value pair exists
if "name" in my_dict:
    print(my_dict["name"])

# looping
for key, value in zip(my_dict.keys(), my_dict.values()):
    print(key, " ", value)

print(my_dict.items())  # .items() returns all key-value pairs

# copying  DONT USE '='
dict1 = my_dict.copy()

# merge 2 dictionaries
# Unexisting fields from dict1 will be added in my_dict
# existing fields in both dicts will be overwritten by dict1
my_dict.update(dict1)
