class Stack:
    def __init__(self, filepath):
        print(f"==== START ====")
        self.filepath = filepath

    def push(self, data):
        try:
            with open(self.filepath, 'r') as file:
                stack = file.readlines()
        
        except FileNotFoundError:
            stack = []
        
        stack.append(f'{data}\n')

        with open(self.filepath, 'w') as file:
            file.write(''.join(stack))

        return data

    def pop(self, idx=-1):
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
        
        except FileNotFoundError:
            raise FileNotFoundError("stack underflow")

        if not lines:
            raise IndexError('stack is empty')
        
        last = lines.pop(idx).strip()

        with open(self.filepath, 'w') as file:
            file.write(''.join(lines))

        return last
    
    def print(self, data):
        if data:
            pass
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
        
        except FileNotFoundError:
            raise FileNotFoundError("stack underflow")

        if not lines:
            return ''

        return lines[-1].strip()
    
    def dump(self):
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
        
        except FileNotFoundError:
            raise FileNotFoundError("stack underflow")

        with open(self.filepath, 'w') as file:
            pass

        return [line.strip() for line in lines]
    
    def stack(self):
        try:
            with open(self.filepath, 'r') as file:
                return [i.strip() for i in file.readlines()]
        
        except FileNotFoundError:
            raise FileNotFoundError("stack underflow")
        
    def dup(self):
        try:
            with open(self.filepath, 'r') as file:
                last = ''.join(file.readlines()[-1]).strip()
        
        except FileNotFoundError:
            raise FileNotFoundError("stack underflow")

        self.push(last)

        return ''

    def swap(self):
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
        
        except FileNotFoundError:
            raise FileNotFoundError("stack underflow")
        
        first = lines.pop()
        second = lines.pop()

        self.push(first)
        self.push(second)

        return ''
    
    def depth(self):
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
        
        except FileNotFoundError:
            raise FileNotFoundError("stack underflow")
        
        return len(lines)
    
    def drop(self):
        with open(self.filepath, 'w'):
            pass

        return ''
    
    def rot(self):
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
        
        except FileNotFoundError:
            raise FileNotFoundError("stack underflow")
        
        first = self.pop(-2)
        second = self.pop(-1)
        third = self.pop(0)
        
        self.push(second)
        self.push(third)
        self.push(first)
        
        return ''