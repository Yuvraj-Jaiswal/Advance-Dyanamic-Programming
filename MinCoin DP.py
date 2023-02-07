
def coin_memo(tar,coins=[1,2,3],memo={}):
    if tar in memo: return memo[tar]
    if tar==0: return 0
    else:
        min_coins = float('inf')
        for coin in coins:
            if tar - coin >= 0:
                min_coins = min(coin_memo(tar-coin,coins)+1,min_coins)
        memo[tar] =min_coins
        return min_coins

def coin_tab(tar,coins=[1,2,3]):
    dp = [float('inf') for _ in range(tar+1)]
    dp[0] = 0
    for i in range(1,len(dp)):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i-coin]+1,dp[i])
    return dp[-1]

print(coin_tab(70))
print(coin_memo(70))


