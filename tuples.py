# Tuple: ordered, immutable, allows duplicate items,
# can't modify existing values

# creating and init
my_tuple = ("Joane", "MArieeee", 14235)
my_tuple = "yes", "no", 1234, "ofc"
my_tuple = ("Name",)  # if 1 element put ',' after, otherwise it's string
my_tuple = tuple(["weiou", 123, 0, 99, "hamster"])

# get the index of an element
print(my_tuple.index("hamster"))

# list from tuple
my_list = list(my_tuple)

# unpacking
my_tuple = ("a", "b", "c", "abc", "def", 137)
i1, *i2, i3 = my_tuple  # i2=all elem between i1,i3 converted to list
print(i1)
print(i2)
print(i3)
