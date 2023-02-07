
def dice_roll(n,m,tar,memo={}):
    if tar < 0 : return 0
    if n==0 and tar==0 : return 1
    if n==0 and tar!=0 : return 0
    if f"{n},{tar}" in memo : return memo[f"{n},{tar}"]
    ways = 0
    for i in range(1,m+1):
        ways += dice_roll(n-1,m,tar-i)
    memo[f"{n},{tar}"] = ways
    return ways

def dice_roll_tab(n,m,tar):
    dp = [ [-1 for _ in range(tar+1)] for _ in range(n+1) ]
    dp[0][0] = 1
    for i in range(1,len(dp[0])):dp[0][i] = 0
    for i in range(1,len(dp)):dp[i][0] = 0

    for dice in range(1,n+1):
        for cur_tar in range(1,tar+1):
            ways = 0
            for i in range(1, m + 1):
                if cur_tar - i >= 0:
                    ways += dp[dice - 1][cur_tar - i]
            dp[dice][cur_tar] = ways
    return dp[-1][-1]

print(dice_roll_tab(5,10,20))
print(dice_roll(5,10,20))