def answer(X, K):
    MIN = pow(10, K-1)
    if(MIN%X == 0):
        return (MIN)
    else:
        return ((MIN + X) - ((MIN + X) % X))
X = 83;  
K = 5;  
print(answer(X, K));
