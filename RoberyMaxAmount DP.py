
def robery_memeo(arr,i=0,seen=[],memo={}):
    if i in memo : return memo[i]
    if i >= len(arr): return 0
    if 0 in seen and i==len(arr)-1: return 0
    else:
        if i == 0:incl = robery_memeo(arr,i+2,seen+[i])+arr[i]
        else: incl = robery_memeo(arr,i+2,seen)+arr[i]
        excl = robery_memeo(arr,i+1,seen)
        result = max(incl,excl)
        memo[i] = result
        return memo[i]

def robery_tab(arr):
    dp = [-1 for _ in range(len(arr))]
    dp[0] = arr[0]
    seen = [0]
    for i in range(1,len(dp)):
        if 0 in seen and i == len(dp)-1:
            dp[i] = dp[i-1]
            break
        incl = dp[i-2]+arr[i]
        excl = dp[i-1]
        dp[i] = max(incl,excl)
    return dp[-1]

print(robery_memeo([9,8,7]))
print(robery_tab([9,8,7]))