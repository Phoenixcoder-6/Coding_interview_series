def knapsack_01(values,weight,w):
    n=len(values)
    dp=[[0 for _ in range(w+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,w+1):
            if weight[i-1]<=w:
                dp[i][w]=max(dp[i-1][w],dp[i-1][w-weight[i-1]]+values[i-1])
            else:
                dp[i][w]=dp[i-1][w]

    return dp[n][w]

values=[60,100,120]
weights=[10,20,30]
capacity=40

max_value=knapsack_01(values,weights,capacity)
print(max_value)