class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
        self.counter = 0 
    def count(self, li, key): 
        if(not li):  
            return self.counter  
        if(li.data == key):  
            self.counter = self.counter + 1 
        return self.count(li.next, key) 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
llist = LinkedList() 
llist.push(1) 
llist.push(3) 
llist.push(1) 
llist.push(2) 
llist.push(1)
elem=int(input('Enter the element to be searched:'))
print('The element appears',llist.count(llist.head,elem),'times')
