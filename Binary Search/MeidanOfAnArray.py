def medianOfArray(A,B):
    def sortedInsert(A,B):
        start = 0
        end = len(A) - 1
        position = -1
        while start <= end:
            #print(start, end)
            mid = (start+end)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                position = max(mid, position)
                #print(mid, position)
                start = mid + 1
            else:
                end = mid - 1
        return position+1
    
    for num in B:
        A.insert(sortedInsert(A,num), num)
    mid = len(A) // 2
    if len(A) % 2 == 0:
        median = (A[mid-1] + A[mid])/2.0
    else:
        median = A[mid]
    return median

A = [0, 23]
B = []
print(medianOfArray(A,B))