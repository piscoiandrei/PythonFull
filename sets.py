# Sets: unordered, mutable, no duplicates

# it will only store non-duplicates
my_set = {1, 2, 3, 5, 10, 1, 2, 3}
my_set = set("Hello")  # stores ('o', 'l', 'H', 'e')
my_set = set()  # empty set

# add items
my_set.add(98)
my_set.add(17)
my_set.add(103)

# remove items
my_set.remove(17)  # error if element doesn't exist
my_set.discard(103)  # no error thrown
my_set.pop()  # removes random value
my_set.clear()

# unions and intersects
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)  # combine elements from 2 sets without duplication
print(u)
i = odds.intersection(evens)
print(i)
i2 = odds.intersection(primes)
print(i2)
u2 = odds.union(primes)
print(u2)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)  # removes the intersection between A and B
diff = setA.symmetric_difference(setB)  # = elements that are not shared

setA.update(setB)  # updates the set by adding the elements that are
# found in the oher set, without duplication
setA.symmetric_difference_update(setB)  # keeps the elements that are
# not shared
setA.intersection_update(setB)  # updates the set by keeping the
# elements that are common
setA.difference_update(setB)  # updates the set by removing the elements
# found in the other set

# SUBSETS & SUPERSET & DISJOINT
setA.issubset(setB)  # adica A inclus in B
setA.issuperset(setB)  # adica B inclus in A
setA.isdisjoint(setB)  # A si B sunt multimi disjuncte

# copying
setA = setB.copy()

# FROZEN SET, updates don't work, besides unions and intersection methods
f = frozenset([1, 3, 4, 5])
