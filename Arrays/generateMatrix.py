def generateMatrix(A):
    matrix = [[0]*A for x in range(A)]
    print(matrix)
    top = 0
    bottom = A - 1
    left = 0
    right = A - 1
    num = 1
    direction = 1
    while top <= bottom and left <= right:
        #direction = direction % 4
        if direction == 1:
            i = left
            while i <= right:
                matrix[top][i] = num
                i += 1
                num += 1
            top+=1
            direction = 2

        if direction == 2:
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            direction = 3
        
        if direction == 3:
            for i in range (right, left-1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -=1
            direction = 4
        
        if direction == 4:
            for i in range (bottom, top-1, -1):
                matrix[i][left] = num
                num += 1
            left +=1
            direction = 1
        
    return matrix
    
print (generateMatrix(4))