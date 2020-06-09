lst=[]
even=0
odd=0
n=int(input('Enter the number of elements:'))
for i in range(0,n):
    b=int(input('Enter element:'))
    lst.append(b)
print('List is:',lst)
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1
print('Count of odd elements:',odd)
print('Count of even elements:',even)
