# python3 chapter-9/tuple.py

x = (1, 2, 3)
print(type(x))


numbers = (10, 20, 30, 40, 50)
n1, n2, n3, n4, n5 = numbers
print(n1, n2, n3, n4, n5)

t = n3, n4
print(type(t))

items = (1, 2, 5.5, ['a', 'b', 'c'], ('apple', 'mango'))
for item in items: 
    print(item, type(item))

li = list(t)
print(li)