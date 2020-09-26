add10 = lambda x: x + 10
print(add10(4))

mult = lambda x, y: x * y
print(mult(10, 3))

points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sorted = sorted(points, key=lambda x: x[1])  # sort by the second elem
print(points_sorted)
points_sorted = sorted(points, key=lambda x: x[0] + x[1])  # sort by sum
print(points_sorted)

a = [1, 2, 3, 4, 5, 6, 7]
b = map(lambda x: x * x, a)
# map() executes a specified function for each item in an iterable
print(list(b))

b = filter(lambda x: x % 2 is 0, a)  # filters elements by bool func
print(list(b))

