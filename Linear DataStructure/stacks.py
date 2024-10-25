class Stack:

    def __init__(self) -> None:
        self.stack = []
    
    count = lambda self: len(self.stack)
    push = lambda self,data: self.stack.append(data)
    is_empty = lambda self: True if len(self.stack) == 0 else False
    pop = lambda self: print("Stack empty") if self.is_empty() else self.stack.pop()
    peek = lambda self: None if self.is_empty() else self.stack[-1]

    def print_stack(self):
        print("HEAD",end=' > ')
        for i in range(-1,(-1*len(self.stack))-1,-1):
            print(f"{self.stack[i]}",end=' -> ')
        print(None)

    '''def push(self,data):

        self.stack.append(data)'''

    '''def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False'''
            

    '''def pop(self):

        if self.is_empty():
            print("Stack Empty, cannot Pop element")
        else:
            return self.stack.pop()'''
    
    '''def peek(self):

        if self.is_empty():
            return "Stack Empty"
        else:
            return self.stack[-1]'''
    
        

def main() -> None:
    stk = Stack()

    stk.push(6)
    stk.push(5)
    stk.push(4)
    stk.push(3)
    stk.push(2)
    stk.push(1)
    stk.push(0)

    print(stk.count())
    print(stk.pek())

    stk.print_stack()    

if __name__ == '__main__':
    main()