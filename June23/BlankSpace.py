#Python program to count the number of blank spaces in a text file
fname = input("Enter file name: ")
k = 0
with open(fname, 'r') as f:
    for i in line:
        if(i. isspace()):
            k=k+1
print("The number of blank spaces is: ",k)
