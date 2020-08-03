def isTriangleExists(a, b, c):
    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180):  
        if((a + b)>= c or (b + c)>= a or (a + c)>= b):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
# Driver Code
a, b, c = 50, 60, 70
print(isTriangleExists(50, 60, 70)) 
