
def min_jump(obs,lane=2,dist=0,memo={}):
    if dist == len(obs)-1: return 0
    key = f'{lane}{dist}'
    if key in memo : return memo[key]
    a1 , a2 = float('inf') , float('inf')

    if obs[dist+1] != lane:
        a1 = min_jump(obs,lane,dist+1,memo)
    else:
        for i in range(1,4):
            if i != lane and obs[dist] != i:
                a2 = min(a2 ,1 + min_jump(obs,lane=i,dist=dist,memo=memo))
    memo[key] = min(a1,a2)
    return memo[key]

def min_jump_dp(obs,lane=2,dist=0,memo=None):
    if memo is None : memo = [[float('inf') for _ in range(len(obs)+1)] for _ in range(4)]
    if dist == len(obs)-1: return 0
    if memo[lane][dist] != float('inf') : return memo[lane][dist]
    a1 , a2 = float('inf') , float('inf')

    if obs[dist+1] != lane:
        a1 = min_jump_dp(obs,lane,dist+1,memo)
    else:
        for i in range(1,4):
            if i != lane and obs[dist] != i:
                a2 = min(a2 ,1 + min_jump_dp(obs,lane=i,dist=dist,memo=memo))
    memo[lane][dist] = min(a1,a2)
    return memo[lane][dist]

def min_jump_tab(obs,dp=None):
    if dp is None : dp = [[float('inf') for _ in range(len(obs))] for _ in range(4)]
    for i in range(0,4):
        dp[i][len(dp[0])-1] = 0

    for cur_ds in range(len(dp[0])-2,-1,-1):
        for cur_ln in range(1,4):
            if obs[cur_ds + 1] != cur_ln:
                dp[cur_ln][cur_ds] = dp[cur_ln][cur_ds + 1]
            else:
                a2 = float('inf')
                for i in range(1, 4):
                    if i != cur_ln and obs[cur_ds] != i:
                        a2 = min(a2, 1 + dp[i][cur_ds+1])
                dp[cur_ln][cur_ds] = a2
    return dp[2][0]

print(min_jump_dp([0,1,2,3,0]))
min_jump_tab([0,1,2,3,0])