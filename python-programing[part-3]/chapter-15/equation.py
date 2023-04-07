# python3 chapter-15/equation.py

def do_operation(operand1, operand2, operator):
    return eval(operand1 + operator + operand2)

def postfix_evaluate(expression):
    operands = []
    operators = '*/-+'

    for character in expression:
        if character.isdigit():
            operands.append(character)
        elif character in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = do_operation(operand1, operand2, character)
            operands.append(str(result))
    
    result = operands.pop()

    return result

def postfix_evaluate_full(expression):
    operands = []
    operators = ["*", "/", "-", "+"]

    expression_list = expression.split(",")

    for item in expression_list:
        if item in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = do_operation(operand1, operand2, item)
            operands.append(str(result))
        else:
            operands.append(item)
    
    result = operands.pop()

    return result


if __name__ == '__main__':
    expression = "20,30,+,2,*,10,*,4,/"
    result = postfix_evaluate_full(expression)
    print(result)