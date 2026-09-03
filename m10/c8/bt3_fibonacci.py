## Dãy Fibonacci: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
# VD: F(3) = F(2)+F(1) = 1+1 = 2
#     F(4) = F(3)+F(2) = 2+1 = 3

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[-1] 


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(5) == 5
assert fibonacci(10) == 55
