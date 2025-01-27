from stack import Stack

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
        
        return stack.push(int(args[0]))
    
    elif op == 'POP':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        return stack.pop(int())
    
    elif op == 'ADD':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = stack.pop()
        rhs = stack.pop()

        return stack.push(lhs + rhs)
    
    elif op == 'SUB':
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = stack.pop()
        rhs = stack.pop()

        return stack.push(lhs-rhs)
    
    elif op == "MUL":
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
        lhs = stack.pop()
        rhs = stack.pop()

        return stack.push(lhs * rhs)
    
    elif op == "DIV":
        if not stack.stack():
            raise ValueError('stack cannot be empty')
        
        if len(stack.stack()) < 2:
            raise ValueError('stack needs 2 elements')
        
    elif op == "PRINT":
        return stack.print()
    
    elif op == "DUMP":
        return stack.dump()
    
    else:
        return

def parse(lines):
    for line in lines.splitlines():
        parseline(line)
    
    print("END")
