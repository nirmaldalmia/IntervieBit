def findDuplicate(A):
    # A.sort()
    # print(A)
    # for i in range(len(A)):
    #     count = A.count(A[i])
    #     if(count > 1):
    #         print(A[i])
    #         return A[i]
    
    # print(-1)
    # return -1
    if len(A) > 1:
        slow = A[0]
        fast = A[A[0]]
        while slow != fast:
            slow = A[slow]
            fast = A[fast]
        
        fast = 0
        while fast != slow:
            slow = A[slow]
            fast = A[fast]
        return slow
    return -1

A = [3,4,1, 4]
findDuplicate(A)