class Stack:
    def __init__(self, filepath):
        print(f"stack initialized\ncheck the stack at {filepath}")
        self.filepath = filepath

    def push(self, data):
        try:
            with open(self.filepath, 'r') as file:
                stack = file.readlines()
        
        except FileNotFoundError:
            stack = []
        
        stack.append(data + '\n')

        with open(self.filepath, 'w') as file:
            file.write(stack)

        return data

    def pop(self):
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
        
        except FileNotFoundError:
            raise FileNotFoundError("stack file not found")

        if not lines:
            raise IndexError('stack is empty')
        
        last = lines.pop().strip()
        lines = lines[:-1].strip()

        with open(self.filepath, 'w') as file:
            file.write(lines)

        return last
    
    def print(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()

        if not lines:
            return ''

        return lines[-1].strip()
    
    def dump(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()

        with open(self.filepath, 'w') as file:
            pass

        return [line.strip() for line in lines]
    
    def stack(self):
        with open(self.filepath, 'r') as file:
            return [i.strip() for i in file.readlines()]