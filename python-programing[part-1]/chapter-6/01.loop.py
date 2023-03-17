# python3 chapter-6/01.loop.py


# for i in range(10):
#     print('I want to be a great programmer')

# import turtle
# turtle.shape("turtle")
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)
# turtle.exitonclick()

# result = 0
# for i in range(50):
#     result = result + 1
# print(result)

# result = 0
# for _ in range(50):
#     result = result + 1
# print(result)

# result = 0
# num = 1
# for _ in range(50):
#     result = result + num
#     num = num + 1
# print(result)

# result = 0
# for num in range(51):
#     result += num
# print(result)

# result = 0
# for num in range(1, 51):
#      result += num
# print(result)

# for i in range(1, 20, 5):
#     print(i)

# numbers = [6, 1, 3, 0, 9, 3, 2, 5]
# max_n = numbers[0]
# for n in numbers:
#     if n > max_n:
#         max_n = n
# print(max_n)

# result = 0
# for num in range(100):
#     if num % 5 == 0:
#         print(num)
#         result += num
# print("Sum is: ", result)

# result = 0
# for num in range(5, 101, 5):
#     print(num)
#     result += num
# print("Sum is: ", result)

import turtle
# turtle.shape("turtle")
turtle.speed(1)

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick()