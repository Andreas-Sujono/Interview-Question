def calculate(firstOperand,operator,secondOperand):
    firstOperand = int(firstOperand)
    secondOperand = int(secondOperand)
    result = -1
    if(operator == '*'):
        result = firstOperand * secondOperand
    elif(operator == '+'):
        result = firstOperand + secondOperand
    elif(operator == '-'):
        result = firstOperand - secondOperand
    elif(operator == '/'):
        result = firstOperand / secondOperand
    else:
        result = firstOperand + secondOperand
    return result


def eval(expression):
    # Fill this in.
    stack = []
    expression = '( '+expression+' )' 
 
    for x in expression:
        if(x == ' '):
            continue
        else:
            stack.append(x)
        while(stack[-1] == ')'):
            print(stack)
            stack.pop() #pop close bracket
            secondOperand = int(stack.pop())
            operator = stack.pop() if stack[-1] !='(' else -1
    
            if(operator != -1 and operator.isdigit()):
                if(stack[-1].isdigit()):
                    stack[-1] = stack[-1] + operator + str(secondOperand)
                else:
                    stack.append(operator + str(secondOperand))
                print(stack)
                stack.append(')')
                continue
            firstOperand = int(stack[-1]) if stack[-1].isdigit() else 0
            stack.pop() if stack[-1] != '(' else None # pop first operand
            if(stack[-1] == '-'):
                stack.pop()
                stack.append('+')
                result = calculate(-firstOperand,operator,secondOperand)
            else:
                result = calculate(firstOperand,operator,secondOperand)
            if(stack[-1] == '('):
                stack.pop()
                stack.append(str(result))
                break
            stack.append(str(result))
            stack.append(')')
            continue
    return int(stack[0])




print eval("1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10")
# -4