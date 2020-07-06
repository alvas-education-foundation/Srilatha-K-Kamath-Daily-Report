#Python Program to Append, Delete and Display Elements of a List Using Classes
class check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def dis(self):
        return (self.n)
obj=check()
choice=1
while choice!=0:
    print("0. Exit 1. Add 2. Delete 3. Display")
    choice=int(input("Enter choice: "))
    if(choice==1):
        n=int(input("Enter number to append: "))
        obj.add(n)
    elif(choice==2):
        n=int(input("Enter number to remove: "))
        obj.remove(n)
    elif(choice==3):
        print("List: ",obj.dis())
    elif(choice==0):
        print("Exiting")
    else:
        print("Invalid choice!!")
print()
