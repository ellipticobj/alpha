# alpha-lang
stack based programming language

# why make this?
i was watching a youtube video (i forgot the name sorry :(..), i got inspired by it to create this. additionally, since i had a school project coming up where i had to create a programming language, i thought itd be a great idea to get the feels of it by starting with this simpler project. 

# roadmap
if else statements  
loops  
jump  
macros  
multiple stack support  
variable support  

# syntax
## push
```
PUSH <val>
```

pushes <val> to the stack

## math
```
ADD
SUB
MUL
DIV
```

does an operation on the top two elements of the stack

## print
```
PRINT
```
prints the top element of the stack

## pop
```
POP
```
removes the top element of the list 

## dump
```
DUMP
```

clears the stack and prints everything

## duplicate
```
DUP
```

duplicates the top element and adds it to the stack

## swap
```
SWAP
```

swaps the top two elements of the stack

## depth
```
DEPTH
```

returns the depth of the stack
