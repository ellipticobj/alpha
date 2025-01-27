from stack import Stack
import sys

stack = Stack('stack.txt')

def parseline(line, stack: Stack):
    tokens = line.split()
    if not tokens:
        return
    
    op = tokens[0].upper()

    args = tokens[1:]

    if op == 'PUSH':
        if not args:
            raise ValueError("you need to push something")
        
        val = args[0]
        
        try:
            stack.push(int(val))
        except ValueError:
            try:
                stack.push(float(val))
            except ValueError:
                try:
                    stack.push(bool(val))
                except ValueError:
                    stack.push(val)

        return ''
    
    elif op == 'POP':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        stack.pop(int())

        return ''
    
    elif op == 'ADD':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = int(stack.pop())
        rhs = int(stack.pop())

        stack.push(lhs + rhs)

        return ''
    
    elif op == 'SUB':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needss 2 elements')
        
        lhs = int(stack.pop())
        rhs = int(stack.pop())

        stack.push(lhs-rhs)
        
        return ''
    
    elif op == "MUL":
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = int(stack.pop())
        rhs = int(stack.pop())

        stack.push(lhs * rhs)

        return ''
    
    elif op == "DIV":
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = int(stack.pop())
        rhs = int(stack.pop())

        stack.push(lhs/rhs)

        return ''
        
    elif op == "PRINT":
        return stack.print()
    
    elif op == "DUMP":
        return stack.dump()
    
    else:
        return ''

def interp(file, stack):
    with open(file, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    idx = 0

    while idx < len(lines):
        out = parseline(lines[idx], stack)
        if out:
            print(out)
        idx += 1

interp(sys.argv[1:], stack)