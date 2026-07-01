## Tổ hợp chập k của n: C(k,n) = n! / (k! * (n-k)!)
# Quy ước: C(0,n) = 1

pass

assert to_hop(0, 5) == 1
assert to_hop(1, 5) == 5
assert to_hop(2, 5) == 10
assert to_hop(3, 5) == 10
assert to_hop(3, 10) == 120
