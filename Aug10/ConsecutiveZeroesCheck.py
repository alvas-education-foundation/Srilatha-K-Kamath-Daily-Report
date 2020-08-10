def hasConsecutiveZeroes(N, K): 
    z = toK(N, K) 
    if (check(z)): 
        print("Yes") 
    else: 
        print("No")  
def toK(N, K): 
    w = 1
    s = 0
    while (N != 0): 
        r = N % K 
        N = N//K 
        s = r * w + s 
        w = w*10
    return s  
def check(N):
    fl = False
    while (N != 0): 
        r = N % 10
        N = N//10
        if (fl == True and r == 0): 
            return False
        if (r > 0): 
            fl = False
            continue
        fl = True
    return True
#main 
N, K = 15, 8
hasConsecutiveZeroes(N, K) 
