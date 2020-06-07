#Python program to Print a list of first and last 5 elements where the values are square of numbers between 1 and 30(both included)
lst=[]
for i in range(1,31):
    sq=i*i
    lst.append(sq)
print('The first 5 elements of the squarred list are:',lst[:5])
print('The last 5 elements of the squarred list are:',lst[-5:])
