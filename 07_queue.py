class Queue:
    def __init__(self):
        self.queue=[];

    def enqueue(self,element):
        self.queue.append(element)

    def isEmpty(self):
        return  len(self.queue)==0;

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue.pop(0);

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'       
        return self.queue[0];

    def display(self):
        if self.isEmpty():
            return 'Queue is empty'
        return list(self.queue)

myqueue=Queue()
myqueue.enqueue(5)
myqueue.enqueue(7)
myqueue.enqueue(6)
myqueue.dequeue()
# myqueue.dequeue()
# myqueue.dequeue()
print(myqueue.display())

        
        