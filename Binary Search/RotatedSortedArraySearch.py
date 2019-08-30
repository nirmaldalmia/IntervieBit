def search(A, B):
    A = list(A)
    n = len(A)
    #print('n = ',n)
    def countRotations(A):
        start = 0
        end = n - 1
        while start <= end:
            mid = int((start+end)/2)
            nextt = (mid+1)%n
            previous = (mid-1+n)%n
            if A[start] < A[end]:
                return start
            elif A[mid] < A[previous] and A[mid] < A[nextt]:
                return mid
            elif A[mid] <= A[end]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
    def binarySearch(A):
        start = 0
        end = len(A) - 1
        #print(start, end)
        while start <= end:
            mid = int((start+end)/2)
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    
    rotations = countRotations(A)
    #print('Rotations: ', rotations)
    if rotations == 0:
        start = 0
        end = n
        #print(start,end)
        result = binarySearch(A[start:end])
        return result
    else:
        start = rotations
        end = n
        #print('case1: ', start, end)
        res = binarySearch(A[start:end])

        if res == -1:
            start = 0
            end = rotations
            res = binarySearch(A[start:end])
            return res
        return (res+rotations)

A = [4, 5, 6, 7, 0, 1, 2]
#A = [0, 1, 2, 3, 4, 5, 6, 7]
B = 8
print(search(A,B))
