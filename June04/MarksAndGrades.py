a=[]
for i in range(0,5):
    b=int(input("Enter mark:"))
    a.append(b)
print("The marks are:",a)
for i in a:
    if(90<=i<=100):
        print("The Mark",i,"is graded A+")
    elif(75<=i<=89):
        print("The Mark",i,"is graded A")
    elif(60<=i<=74):
        print("The Mark",i,"is graded B+")
    elif(40<=i<=59):
        print("The Mark",i,"is graded B")
    else:
        print("The Mark",i,"is graded C")
