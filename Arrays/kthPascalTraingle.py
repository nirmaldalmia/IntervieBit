class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow():
        array = []
        A = 3
        for i in range (0,A+1):
            list = []
            for j in range (0,i+1):
                if (i==j or j==0):
                    list.insert(j, 1)
                else:
                    value = array[i-1][j-1] + array[i-1][j]
                    list.append(value)
            array.append(list)
        
        return (array[A])

test = Solution.getRow()