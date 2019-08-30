def searchRange(A,B):
    def findLeft(A,B):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = int((start+end)/2)
            if A[mid] == B:
                if A[mid] == 0 or A[mid - 1] != B:
                    return mid
                end = mid - 1   
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def findRight(A,B):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = int((start+end)/2)
            if A[mid] == B:
                if mid + 1 >= len(A) or A[mid + 1] != B:
                    return mid
                start = mid + 1
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1   
        return -1
    
    return ([findLeft(A,B), findRight(A,B)])

A = [5, 7, 7, 8, 8, 10]
B = 8
print(searchRange(A,B))