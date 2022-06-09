class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self,x):
        self.stack.append(x)
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return self.size() == 0
    
    def pop(self):
        if not self.empty():
            return self.stack.pop(-1)
    def top(self):
        if not self.empty():
            return self.stack[-1]
    
def solution(s):
    parenthesis_stack = Stack()
    
    for ch in s:
        if ch == '(':
            parenthesis_stack.push(ch)
        else :
            if parenthesis_stack.empty():
                return False
            parenthesis_stack.pop()
    else :
        if not parenthesis_stack.empty():
            return False
        return True