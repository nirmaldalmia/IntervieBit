def findCount(A,B):
    A = list(A)
    def findOccurence(Arr, B, searchFirst):
        #A = list(A)
        start = 0
        end = len(A)
        result = -1
        while start <= end-1:
            mid = (start + end) // 2
            print(start, mid, end)
            if A[mid] == B:
                result = mid
                if searchFirst:
                    end = mid - 1
                else:
                    start = mid + 1
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1
        return result
        
    firstOccurence = findOccurence(A, B, True)
    lastOccurence = findOccurence(A, B, False)
    print(firstOccurence, lastOccurence)
        
    count = len(A[firstOccurence:lastOccurence + 1])
    return count

A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 10
print(findCount(A,B))