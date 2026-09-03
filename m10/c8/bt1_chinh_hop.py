## Chỉnh hợp chập k của n: A(k,n) = n! / (n-k)!
# Quy ước: A(0,n) = 1

def giai_thua(n):
    gt = 1
    for i in range(1,n+1):
        gt *= i
    return gt

def chinh_hop(k, n):
    return giai_thua(n)/ giai_thua(n-k)

assert chinh_hop(0, 5) == 1
assert chinh_hop(1, 5) == 5
assert chinh_hop(2, 5) == 20
assert chinh_hop(3, 5) == 60
assert chinh_hop(3, 10) == 720
