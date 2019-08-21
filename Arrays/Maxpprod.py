def maxSpecialProduct(A):
    maxProd = 0
    LeftMaxIndex = 0
    RightMinIndex = 0
    for i in range(1, len(A) - 1):
        LeftMaxIndex = 0
        RightMinIndex = 0
        for j in range(i,0,-1):
            if A[j] > A[i]:
                LeftMaxIndex = j
                break
        for k in range(i+1, len(A)):
            if A[k] > A[i]:
                RightMinIndex = k
                break
        #print(LeftMaxIndex, RightMinIndex)
        currentMaxProd = LeftMaxIndex*RightMinIndex
        if(currentMaxProd > maxProd):
            maxProd = currentMaxProd % 1000000007
    #maxProd = (LeftMaxIndex*RightMinIndex)%1000000007
    return (maxProd)

#A = [4, 6, 5, 5, 6, 6, 5, 6, 7, 5, 5, 7, 7]
A = [5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]
print(maxSpecialProduct(A))


