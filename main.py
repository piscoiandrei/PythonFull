from itertools import *

a = [1, 2]
b = [3, 4]
prod = product(a, b)  # produsul cartezian dintre A si B
print(list(prod))

c = [1, 2, 3]
print('c')
perm_length = 2
perm = permutations(c, perm_length)
print(list(perm))

d = [1, 2, 3, 4]
print('d')
cmb_len = 3
cmb = combinations(d, cmb_len)
print(list(cmb))

e = [1, 2, 3, 4, 5]  # poti sa ai si accumulate(e,func=my_func/lambda)
print('e')
acc = accumulate(e)  # elementul n e suma elementelor pana la el inclusiv
print(list(acc))

f = [1, 2, 3, 4, 5, 6]
print('f')
group_obj = groupby(f, key=lambda x: x < 3)  # grouping by function condition
for key, value in group_obj:
    print(key, list(value))

