class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element);
    
    def isEmpty(self):
        return len(self.stack)==0;

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop();

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    
    def display(self):
        if self.isEmpty():
            return 'stack is empty'
        return "-->".join(map(str,reversed(self.stack)))
    
mystack=Stack();
mystack.push(3)
mystack.push(4)
mystack.push(5)
mystack.push(6)
mystack.pop();
print(mystack.display());
        
