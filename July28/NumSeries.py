def PrintNumber(N, Original, K, flag):
    print(N, end = " ")
    if (N <= 0):
        if(flag==0):
            flag = 1
        else:
            flag = 0
    if (N == Original and (not(flag))):
        return
    if (flag == True):
        PrintNumber(N - K, Original, K, flag)
        return
    if (not(flag)):
        PrintNumber(N + K, Original, K, flag)
        return
N = 20
K = 6
print(PrintNumber(N, N, K, True))
