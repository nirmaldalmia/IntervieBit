def maxDistance(A):
    n = len(A)
    index = dict()
    for i in range(n):
        if A[i] in index:
            index[A[i]].append(i)
        else:
            index[A[i]] = [i]
    A.sort()
    maxDiff = -1
    temp = n
    #print('Index of greatest: ',)
    #print(index)
    #print(A)
    for i in range(n):
        indexi = index[A[i]][0]
        if temp > indexi:
            temp= indexi
        maxDiff = max(maxDiff, index[A[i]][-1] - temp)
    return maxDiff



A = [3,5,4,2]
print(maxDistance(A))