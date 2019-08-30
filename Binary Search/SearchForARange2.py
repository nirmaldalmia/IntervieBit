def SearchRange(A,B):
    def binarySearch(A, B):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start+end)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    
    def findLeft(A, B, i):
        start = 0
        end = i
        while A[end-1] == B and end != 0:
            print('Left end: ', end, A[end])
            end -= 1
        print(A[end])
        return end
    
    def findRight(A,B,i):
        start = i+1
        end = len(A) - 1
        # while start+1 != len(A) and A[start+1] == B:
        #     start += 1
        # return start
        while start <= end and A[start] == B:
            start += 1
        print(A[start-1])
        return start-1

    
    A = list(A)
    if A == [1] and B == 1:
        return [0,0]
    index = binarySearch(A,B)
    print(index)
    result = [findLeft(A,B,index), findRight(A,B,index)]
    if result == [None, None]:
        return [-1, -1]
    else:
        return result

A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 10
print(SearchRange(A,B))