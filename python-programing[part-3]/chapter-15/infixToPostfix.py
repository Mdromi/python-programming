# python3 chapter-15/infixToPostfix.py

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if self.items == []:
            return True
        return False

def infix_to_postfix(expression):
    precedence = {}
    precedence['/'] = 2
    precedence['*'] = 2
    precedence['-'] = 1
    precedence['+'] = 1

    operators = Stack()
    postfix = []

    for item in expression:
        if item.isdigit():
            postfix.append(item)
        elif item in "*/-+":
            while operators.is_empty() is False:
                op = operators.pop()
                if precedence[op] >= precedence[item]:
                    postfix.append(op)
                else:
                    operators.push(op)
                    break
            operators.push(item)
    
    while operators.is_empty() is False:
        op = operators.pop()
        postfix.append(op)
    
    return " ".join(postfix)


if __name__ == "__main__":
   expression = "1 + 2 + 3 * 4 - 5"
   postfix_exp = infix_to_postfix(expression)
   print(postfix_exp)