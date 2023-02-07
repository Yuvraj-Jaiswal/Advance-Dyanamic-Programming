
def maxsum_memo(arr,i=0,memo={}):
    if i in memo: return memo[i]
    if i >= len(arr): return 0
    else:
        sum1 = maxsum_memo(arr,i+2,memo)+arr[i]
        sum2 = maxsum_memo(arr,i+1,memo)
        result = max(sum1, sum2)
        memo[i] = result
        return result

def maxsum_tab(arr):
    dp = [-1 for _ in range(len(arr))]
    dp[0] = arr[0]
    for i in range(1,len(dp)):
        if i-2 >= 0:
            incl = dp[i-2] + arr[i]
            excl = dp[i-1]
            dp[i] = max(incl,excl)
        elif i-1==0:dp[i] = dp[i-1]
    return dp[-1]

def maxsum_sp(arr):
    prev1 = arr[0]
    prev2 = 0
    ans = -1
    for i in range(1,len(arr)):
        inc = prev2+arr[i]
        exc = prev1
        ans = max(inc,exc)
        prev2 = prev1
        prev1 = ans
    return ans


print(maxsum_memo([9,9,8,-2,-2]))
print(maxsum_tab([9,9,8,-2,-2]))
print(maxsum_sp([9,9,8,-2,-2]))