def sort(A):
    n = len(A)
    i = 1
    while i < n:
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        i += 1
    return A

A = [3, 5, 4, 1]
sort(A)
print(A)
