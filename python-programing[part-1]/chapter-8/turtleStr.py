# python3 chapter-8/turtleStr.py

import turtle 

name = turtle.textinput('name', 'What is your name?')
name = name.lower()

if name.startswith('mr'):
    print('Hello Sir, How can i help you?')

elif name.startswith('mrs') or name.startswith('miss') or name.startswith('ms'):
    print('Hello Mam, How are you?')
else:
    name = name.capitalize()
    str = 'Hi ' + name + '! How are you?'
    print(str)

turtle.exitonclick()
