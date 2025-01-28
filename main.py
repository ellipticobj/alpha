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

        return '', idx+1
    
    elif op == 'POP':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        stack.pop(int())

        return '', idx+1
    
    elif op == "PRINT":
        return stack.print(args), idx+1
    
    elif op == "DUMP":
        return stack.dump(), idx+1
    
    elif op == "STACK":
        return stack.stack(), idx+1
    
    elif op == "DUP":
        return stack.dup(), idx+1
    
    elif op == "SWAP":
        return stack.swap(), idx+1
    
    elif op == "DEPTH":
        return stack.depth(), idx+1
    
    elif op == "DROP":
        return stack.drop(), idx+1
    
    elif op == 'ADD':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        # TODO: limit these to only ints and floats
        
        lhs = stack.pop()
        rhs = stack.pop()

        stack.push(lhs + rhs)

        return '', idx+1
    
    elif op == 'SUB':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = int(stack.pop())
        rhs = int(stack.pop())

        stack.push(lhs-rhs)
        
        return '', idx+1
    
    elif op == "MUL":
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = int(stack.pop())
        rhs = int(stack.pop())

        stack.push(lhs * rhs)

        return '', idx+1
    
    elif op == "DIV":
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = int(stack.pop())
        rhs = int(stack.pop())

        stack.push(lhs/rhs)

        return '', idx+1
    
    elif op == 'EQ':
        if len(stack.stack()) < 2:
            raise ValueError("stack needs 2 elements")
        a = stack.pop()
        b = stack.pop()
        stack.push(a == b)
        return '', idx+1

    elif op == 'LT':
        if len(stack.stack()) < 2:
            raise ValueError("stack needs 2 elements")
        a = stack.pop()
        b = stack.pop()
        stack.push(a < b)
        return '', idx+1

    elif op == 'GT':
        if len(stack.stack()) < 2:
            raise ValueError("stack needs 2 elements")
        a = stack.pop()
        b = stack.pop()
        stack.push(a > b)
        return '', idx+1
    
    elif op == 'LABEL':
        return '', idx+1
    
    elif op == 'JUMP':
        if not tokens[1:]:
            return SyntaxError('jump needs an argument')
        labelname = tokens[1]
        if labelname not in set(labels.keys()):
            raise ValueError(f'label {labelname} not found')
        
        idx = labels[labelname]
        return '', idx+1
    
    else:
        return '', idx+1
    
def marklabels(lines):
    # TODO: debug
    global labels
    labels = {}
        
    for idx in range(len(lines)):
        if lines[idx].startswith('LABEL'):
            labels[lines[idx].split()[1]] = idx

def interp(file, stack):
    with open(file, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        
    marklabels(lines)

    idx = 0

    while idx < len(lines):
        out, idx = parseline(lines, idx, stack)
        
        if out:
            print(out)


args = sys.argv[1:]
for file in args:
    interp(file, stack)
    
print("===== END =====")