from classes import *

e1 = Employee("Valentin", "Ancau", 200)

d1 = Developer("Andrei", "Piscoi", 1300000099, "Python")

print(e1.email)
print(d1.email)

d1.apply_raise(10)
e1.apply_raise(0.1)

print(e1.salary)
print(d1.salary)
