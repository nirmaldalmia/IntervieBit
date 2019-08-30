def solve(A):
    A.sort()
    n = len(A)
    for i in range(n):
        greaterNumbers = len(A[i+1:n])
        #print(greaterNumbers, A[i], i)
        if greaterNumbers == A[i]:
            #print(len(A[i+1:-1]), A[i])
            return 1
    return -1

A = [ -4, -2, 0, -1, -6]
print(solve(A))