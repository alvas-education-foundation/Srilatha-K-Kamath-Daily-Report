#Python Program to Create a Class in which One Method Accepts a String from the User and Another Prints its.
class demoprint():
    def __init__(self):
        self.string=""
    def get(self):
        self.string=input("Enter string: ")
    def put(self):
        print("String is:")
        print(self.string)
obj=demoprint()
obj.get()
obj.put()
