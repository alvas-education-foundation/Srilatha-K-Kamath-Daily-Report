mydict={}
n=int(input('Enter no. of entries:'))
for i in range(0,n):
    key = input("Enter the name: ")
    value = int(input("Enter the marks: "))
    mydict[key] = value
print(mydict)
sum=0
for value in mydict:
    sum+=mydict[value]
avrg=sum/n
print('Average Is:',avrg)
    
