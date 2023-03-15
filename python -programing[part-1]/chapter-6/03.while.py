# python3 chapter-6/03.while.py 

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# i = 5
# while i >= 0:
#     i -= 1
#     print(i)

# n = input("Please enter a positive integer: ")
# n = int(n)

# m = 1
# while m <=10:
#     print(n, 'x', m, '=', n*m)
#     m += 1


# import turtle
# turtle.color("yellow")
# turtle.speed(5)

# counter = 0
# while counter < 36:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(10)
#     counter += 1
# turtle.exitonclick()


# import turtle
# height = 5
# width = 5
# turtle.speed(2)
# turtle.penup()

# for y in range(height):
#     for x in range(width):
#         turtle.dot()
#         turtle.forward(20)
#     turtle.backward(20 * width)
#     turtle.right(90)
#     turtle.forward(20)
#     turtle.left(90)
# turtle.exitonclick()

# while True:
#     n = input('Please enter a number (0 to exit): ')
#     n = int(n)
#     if n == 0:
#         break
#     print("Square of", n, 'is', n*n)

# while True:
#     n = input('Please enter a positive number (0 to exit): ')
#     n = int(n)
#     if n < 0:
#         print('Only allow positive number. Please try again.')
#         continue
#     if n == 0:
#         break
#     print("Square of", n, 'is', n*n)

terminate = False
while not terminate:
    number1 = input('Please enter a number: ')
    number1 = int(number1)
    number2 = input('Please enter another number: ')
    number2 = int(number2)
    while True:
        operation = input('Please enter add/sub or quit to exit:')
        if(operation == 'quit'):
            terminate = True
            break
        if operation not in ['add', 'sub']:
            print('Unknown operator !')
            continue
        if operation == 'add':
            print("Result is", number1 + number2)
            break
        if(operation == 'sub'):
            print('Result is', number1 - number2)
            break
