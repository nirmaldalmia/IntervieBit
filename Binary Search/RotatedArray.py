def findMin(A):
    A = list(A)
    n = len(A)
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = int((start+end)/2)
        nextt = (mid + 1)%n
        previous = (mid - 1 + n) % n
        if A[start] < A[end]:
            return A[start]
        elif A[mid] <= A[nextt] and A[mid] <= A[previous]:
            return A[mid]
        elif A[mid] <= A[end]:
            end = mid -1
        else:
            start = mid + 1