# python3 chapter-9/set.py

li = [1, 2, 3, 4]
tpl = (1, 2, 3)

A = set(li)
B = set(tpl)
print(type(A))
print(type(B))

A = set("apple")
print(A)
print('a' in A)


A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8}

C = A & B
print(C)

C = A | B
print(C)

C = A ^ B
print(C)

C = A - B
print(C)