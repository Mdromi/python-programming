# python3 chapter-10/randomNum.py

import random
import turtle

print(random.random())
print(random.randint(10, 50))
print(random.randint(3, 9))

# list of colors 
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'purple']
turtle.penup()
for i in range(50):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    turtle.setposition(x, y)
    i = random.randint(0, len(colors) - 1)
    turtle.dot(colors[i])
turtle.done()