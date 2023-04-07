# python3 chapter-13/countSort.py

L = [3, 4, 1, 6, 2, 4, 9, 7, 8, 4, 2, 1]

count = [0] * 11
for x in L:
    count[x] = count[x] + 1

sorted_list = []
for index, value in enumerate(count):
    if value > 0:
        sorted_list.extend([index] * value)

print(sorted_list)