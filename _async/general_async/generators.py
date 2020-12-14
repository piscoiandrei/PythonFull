"""
 PROS: memory and time efficiency - working with one value at a time
"""


def process_objects(objects):
    for obj in objects:
        """
        Do some processing on the object then return one result at a time.

        The function gets suspended after the yield statement
        and comes back where it left off
        """
        result = str(obj) + " has been processed"
        yield result


my_gen = process_objects([1, 2.132, 'bacon'])
print(my_gen)

# another way to create a generator
my_gen = (str(o) + " done" for o in ['meal', 2.13, 'yes'])
print(my_gen)

# create a list from a generator
my_list = list(my_gen)

for res in my_gen:
    print(res)
