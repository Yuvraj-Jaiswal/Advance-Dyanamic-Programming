
def starecae_memo(n,steps=[1,2],memo={}):
    if n in memo: return memo[n]
    if n == 0 : return 1
    else:
        ways = 0
        for step in steps:
            if n-step >= 0:
                ways += starecae_memo(n-step,steps,memo)
        memo[n] = ways
        return ways

def staircase_tab(n,dp=None):
    if dp is None : dp = [-1 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    if dp[n] != -1: return dp[n]
    else:
        for i in range(3,len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

print(staircase_tab(12))
print(starecae_memo(12))


