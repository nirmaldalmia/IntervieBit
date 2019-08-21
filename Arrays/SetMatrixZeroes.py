def setZeroes(A):
    listA = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                listA.append((i,j))
    for x in listA:
        #print(x[0], x[1])
        A[x[0]] = [0]*len(A[0])
        for j in range(len(A)):
            A[j][x[1]] = 0
    #print(listA)
    print(A)

#A = [[1, 0, 1],
#    [1, 1, 1],
#    [1, 1, 1]]
A = [[0,0], [1,1]]
setZeroes(A)