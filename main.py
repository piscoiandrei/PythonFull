from classes import *

c = City("JHGQd", "fwef", 123, 13)

c1 = eval(c.__repr__())
c2 = eval(repr(c))
print(type(c))
print(type(c1))

print(c+c1)
print(c.population)
