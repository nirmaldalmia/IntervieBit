def subUnsort(A):
    temp = sorted(A)
    if temp == A:
        return [-1]
    n = len(A)
    for s in range(1, n-1):
        if A[s] > A[s+1]:
            break
    e = n-1
    while e > 0:
        if A[e] < A[e-1]:
            break
        e -=1
    print(s,e)
    minx = min(A[s:e+1])
    maxx = max(A[s:e+1])
    # max = A[s]
    # min = A[s]
    for i in range(s):
        if A[i] > minx:
            s = i
            break
    for i in range(n-1, e, -1):
        if A[i] < maxx:
            e = i
            break
    return [s,e]

A = [ 10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60 ]
print(subUnsort(A))