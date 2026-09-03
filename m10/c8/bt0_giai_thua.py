## Giai thừa: n! = 1 * 2 * 3 * ... * n
# Quy ước: 0! = 1

def giai_thua(n):
    gt = 1
    for i in range(1,n+1):
        gt *= i
    return gt

assert giai_thua(0) == 1
assert giai_thua(1) == 1
assert giai_thua(5) == 120
assert giai_thua(10) == 3628800
