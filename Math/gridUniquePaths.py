def uniquePaths(m,n):
    dp = [1 for i in range(n)]
    for i in range(0,m-1):
        for j in range(1,n):
            dp[j] += dp[j-1]
    return dp[n-1]

print(uniquePaths(3,3))