# python3 chapter-9/list.py

sarrc = ["Bangladesh", "Afganistan", "Bhutan", "Nepal", "India", "Pakistan"]

sarrc.append("Sri Lanka")
sarrc.insert(0, "BD")
print(sarrc)

sarrc.sort()
print(sarrc)

sarrc.reverse()
print(sarrc)

des = "BD"
if des in sarrc:
    sarrc.remove(des)
else :
    print(des, 'not in list')

print(sarrc.pop(1))

li = [1, 3, 4, 2]
li2 = [4, 6, 5, 9]
li.extend(li2)
li.sort()
print(li)

del (li[0])
del (li)

li = []
for x in range(10):
    li.append(x)
print(li)

cunt = "-".join(sarrc)
print(cunt)

# List comprehensions
new_li = [2 * x for x in li2]
print(new_li)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
even_numbers = [x for x in li if x % 2 == 0]
print(even_numbers)

squares = [n**2 for n in li2]
print(squares)
