## Tổ hợp chập k của n: C(k,n) = n! / (k! * (n-k)!)
# Quy ước: C(0,n) = 1

def giai_thua(n):
    gt = 1
    for i in range(1,n+1):
        gt *= i
    return gt

def to_hop(k, n):
    return giai_thua(n)/ (giai_thua(n-k)*giai_thua(k))

assert to_hop(0, 5) == 1
assert to_hop(1, 5) == 5
assert to_hop(2, 5) == 10
assert to_hop(3, 5) == 10
assert to_hop(3, 10) == 120
