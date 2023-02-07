
def knapsack(weight,value,capacity,i=None,memo={}):
    if i is None : i = len(weight)-1

    if f'{i},{capacity}' in memo : return memo[f'{i},{capacity}']
    if i == 0 :
        if capacity - weight[i] >= 0:
            return value[i]
        else:return 0

    taken = -1
    if capacity-weight[i] >= 0:
        taken = value[i] + knapsack(weight,value,capacity-weight[i],i-1,memo)
    nottaken = knapsack(weight,value,capacity,i-1,memo)
    memo[f'{i},{capacity}'] = max(taken,nottaken)
    return memo[f'{i},{capacity}']


def knapsack_tab(weight,value,capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(value))]

    for w in range(len(dp[0])):
        if weight[0] <= w:
            dp[0][w] = value[0]
        else:dp[0][w] = 0

    for idx in range(1,len(dp)):
        for cap in range(len(dp[0])):
            taken = -1
            if cap - weight[idx] >= 0:
                taken = value[idx] + dp[idx - 1][cap - weight[idx]]
            nottaken = dp[idx - 1][cap]
            dp[idx][cap] = max(taken,nottaken)
    return dp[-1][-1]

def knapsack_tab_SpaceOptimization(weight,value,capacity):
    prev = [0 for _ in range(capacity+1)]
    curr = [0 for _ in range(capacity+1)]

    for w in range(len(prev)):
        if weight[0] <= w:
            prev[w] = value[0]
        else:prev[w] = 0

    for idx in range(1,len(value)):
        for cap in range(len(prev)):
            taken = -1
            if cap - weight[idx] >= 0:
                taken = value[idx] + prev[cap - weight[idx]]
            nottaken = prev[cap]
            curr[cap] = max(taken,nottaken)
        prev = curr

    return curr[-1]

print(knapsack_tab([1,2,4,5],[5,4,8,6],5))
print(knapsack([1,2,4,5],[5,4,8,6],5))
print(knapsack_tab_SpaceOptimization([1,2,4,5],[5,4,8,6],5))