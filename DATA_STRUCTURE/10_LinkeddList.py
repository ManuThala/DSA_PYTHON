class Node:    
    def __init__(self,data=None,next=None):        
        self.value = data        
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_begining(self,data):
        node=Node(data,self.data)   
        