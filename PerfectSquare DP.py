
def perfect_sq_min(n,memo={}):
    if n <= 0 : return 0
    if n in memo : return memo[n]
    i = 1
    ans = float('inf')
    while i*i <= n:
        ans = min(1+perfect_sq_min(n-i*i),ans)
        i += 1
    memo[n] = ans
    return ans

def perfect_sq_tab(n):
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    for k in range(1,len(dp)):
        i = 1
        ans = float('inf')
        while i * i <= n :
            ans = min(1 + dp[k - i * i], ans)
            i += 1
        dp[k] = ans
    return dp[-1]

print(perfect_sq_min(11))
print(perfect_sq_tab(11))