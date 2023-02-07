
def rodcutting_memo(n,parts=[5,2,2],memo={}):
    if n in memo: return memo[n]
    if n <= 0 : return 0
    else:
        ways = -float('inf')
        for part in parts:
            if n-part >= 0:
                ways = max(1+rodcutting_memo(n-part,parts,memo),ways)
        memo[n] = ways
        return ways

def rodcutting_tab(n,parts=[5,2,2]):
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    for i in range(1,n+1):
        for part in parts:
            if i-part >= 0:
                dp[i] = max(dp[i-part]+1,dp[i])
    return dp[-1]

print(rodcutting_memo(3))
print(rodcutting_tab(3))