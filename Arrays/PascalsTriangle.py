class Solution:
    def solve():
        array = []
        def binomialCoeff(n, k) :
            res = 1
            if (k > n - k) : 
                k = n - k 
            for i in range(0 , k) : 
                res = res * (n - i) 
                res = res // (i + 1) 
            return res

        A = 5
        for i in range (0, A):
            #print(i)
            list = []
            for j in range (0,i+1):
                #print(j)
                value = binomialCoeff(i,j)
                list.append(value)
            array.append(list)
        return array

        

test = Solution.solve()
# test.solve()