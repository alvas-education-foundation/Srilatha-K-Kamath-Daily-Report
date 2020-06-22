filename=input("Enter file name: ")
with open (filename,'r') as f:
    for line in f:
        l=line.split()
        l.reverse() 
        st= " ".join(l)
        print (st)
