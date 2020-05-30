# Python Program to Reverse a Number
number = int(input("Please Enter any Number: "))
Reverse = 0
while(number > 0):
    Reminder = number %10
    Reverse = (Reverse *10) + Reminder
    number = number //10
print("\nReverse of entered number is = %d" %Reverse)
