class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self): 
        self.head = None
    def count(self, search_for): 
        current = self.head 
        count = 0
        while(current is not None): 
            if current.data == search_for: 
                count += 1
            current = current.next
        return count 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next
llist = LinkedList() 
llist.push(1) 
llist.push(3) 
llist.push(1) 
llist.push(2) 
llist.push(1) 
elem=int(input('Enter element to be searched:'))
print('The element appears',llist.count(elem),'times')
