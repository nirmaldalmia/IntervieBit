def sortedInsert(A, B):
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
    



A = [1,3,5,6]
B = 0
print(sortedInsert(A,B))