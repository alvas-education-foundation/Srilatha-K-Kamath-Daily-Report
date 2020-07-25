def answer(X, K): 
    MAX = pow(10, K) - 1
    return (MAX - (MAX % X)) 
X = 30;  
K = 3;  
print(answer(X, K));  
