from stack import Stack
import sys

stack = Stack('stack.txt')
labels = {}

def parseline(lines, idx, stack: Stack):
    line = lines[idx].strip()
    tokens = line.split()
    if not tokens:
        return
    
    op = tokens[0].upper()

    args = tokens[1:]

    if op == 'PUSH':
        if not args:
            raise ValueError("you need to push something")
        
        val = args[0].lower()
        
        if val in {'true', 'false'}:
            stack.push(val == 'true')
        else:
            try:
                stack.push(int(val))
            except:
                try:
                    stack.push(float(val))
                except:
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
        
        # TODO: limit these to only ints and floats
        
        lhs = stack.pop()
        rhs = stack.pop()

        stack.push(lhs + rhs)

        return ''
    
    elif op == 'SUB':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
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
    
    elif op == 'EQ':
        if len(stack.stack()) < 2:
            raise ValueError("stack needs 2 elements")
        a = stack.pop()
        b = stack.pop()
        stack.push(a == b)
        return ''

    elif op == 'LT':
        if len(stack.stack()) < 2:
            raise ValueError("stack needs 2 elements")
        a = stack.pop()
        b = stack.pop()
        stack.push(a < b)
        return ''

    elif op == 'GT':
        if len(stack.stack()) < 2:
            raise ValueError("stack needs 2 elements")
        a = stack.pop()
        b = stack.pop()
        stack.push(a > b)
        return ''
    
    elif op == 'LABEL':
        return ''
    
    elif op == 'JUMP':
        # TODO: make jumps
        return ''
    
    else:
        return ''
    
def marklabels(lines):
    # TODO: debug
    global labels
    labels = {}
        
    for idx in len(lines):
        if lines[idx].startswith('LABEL'):
            labels[lines[idx][1]] = idx

def interp(file, stack):
    with open(file, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        
    marklabels(lines)

    idx = 0

    while idx < len(lines):
        out = parseline(lines, idx, stack)
        
        if out:
            print(out)
        idx += 1

interp(sys.argv[1:], stack)