def checkDivisibility(n, digit) :
    return (digit != 0 and n % digit == 0)
def allDigitsDivide( n) :
    temp = n
    while(temp > 0):
        digit = n % 10
        if ((checkDivisibility(n, digit)) == False):
            return False
        temp = temp // 10
    return True
#main
n = int(input('Enter a number:'))
if (allDigitsDivide(n)) :
    print("Yes")
else :
    print("No" ) 
