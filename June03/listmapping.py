L=[]
n=int(input("Enter no of entries:"))
for i in range(0,n):
    a=int(input("Enter roll no.s:"))
    L.append(a)
M=[]
for i in range(0,n):
    b=int(input("Enter marks:"))
    M.append(b)
D={}
for roll in L:
    for marks in M:
        D[roll]=marks
print("The dictionary is:",D)        
