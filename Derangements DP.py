
def derangements(n,memo={}):
    if n == 1 : return 0
    if n == 2 : return 1
    if n in memo : return memo[n]
    else:
        result = (n-1)*(derangements(n-1)+derangements(n-2))
        memo[n] = result
        return memo[n]

def derangements_tab(n):
    dp = [-1 for _ in range(n+1)]
    dp[1] = 0
    dp[2] = 1
    for i in range(3,len(dp)):
        dp[i] = (i-1)*(dp[i-1]+dp[i-2])
    return dp[-1]

def derangements_sp(n):
    first = 0
    second = 1
    for i in range(3,n):
        ans = (i-1)*(dp[i-1]+dp[i-2])
    return dp[-1]

print(derangements(10))
print(derangements_tab(10))

