
def fibonachi_memo(n,memo={0:1,1:1}):
    if n == 0 or n == 1:
        return n
    if n in memo: return memo[n]
    else:
        result = fibonachi_memo(n-1)+fibonachi_memo(n-2)
        memo[n] = result
        return result


def fibonachi_tab(n):
    if n == 0 or n == 1: return n
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]


def fibonachi_sopt(n):
    if n == 0 or n == 1: return n
    first = 0
    second = 1
    for i in range(2,n+1):
        nxt = first + second
        first = second
        second = nxt
    return second

print(fibonachi_sopt(10))