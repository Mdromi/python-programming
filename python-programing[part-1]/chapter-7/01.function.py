# python3 chapter-7/01.function.py

# def add(n1, n2):
#     return n1 + n2

# n = 10
# m = 5
# result = add(n, m)
# print(result)

# number1 = 10
# number2 = 10
# result = add(number1, number2)
# print(result)

# n1 = 20
# n2 = 10
# print(add(n1, n2))

# print(add(2.5, 3.5))

# import turtle
# turtle.color('blue')
# turtle.speed(8)
# def draw_square(side_length):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)
# counter = 0
# while counter < 90:
#     draw_square(100)
#     turtle.right(4)
#     counter += 1
# turtle.exitonclick()

# import turtle
# turtle.color('blue')
# turtle.speed(8)
# def draw_triangle(side_length):
#     for i in range(3):
#         turtle.forward(side_length)
#         turtle.left(120)
# counter = 0
# while counter < 1:
#     draw_triangle(100)
#     turtle.right(4)
#     counter += 1
# turtle.exitonclick()

# def myfunc(x):
#     print('inside my func', x)
#     x = 10
#     print('inside my func', x)

# x = 20
# myfunc(x)
# print(x)

# def myfunc(y):
#     print("y =", y)
#     print("x =", x)
# x = 20
# myfunc(x)

# def myfunc(y = 10):
#     print("y =", y)
# x = 20
# myfunc(x)
# myfunc()

# def myfunc(x, y = 10, z = 0):
#     print("x =", x, "y =", y, "z = ", z)

# x = 5
# y = 6
# z = 7
# myfunc(x, y, z)
# myfunc(x, y)
# myfunc(x)

# def myfunc(x, z, y = 10):
#     print("x =", x, "y =", y, "z = ", z)

# myfunc(x = 1, y = 2, z = 5)
# a = 5
# b = 6
# myfunc(x = a, z = b)
# a = 1
# b = 2
# c = 3
# myfunc(y = a, z = b, x = c)

# def add_numbers(numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     return result
# result = add_numbers([1, 2, 30, 4, 5, 9])
# print(result)

# def test_fnc(li):
#     li[0] = 10
# my_list = [1, 3, 3, 4]
# print('before function call', my_list)
# test_fnc(my_list)
# print('after function call', my_list)

# list1 = [1, 3, 3, 4]
# list2 = list1
# print(list1)
# print(list2)
# list2[0] = 100
# print(list2)
# print(list1)

li = [1, 2, 3]
result = sum(li)
print(result)