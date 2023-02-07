
def ticket_min(days,cost,i=0,memo={}):
    if i >= len(days):return 0
    if i in memo : return memo[i]

    pass1 = ticket_min(days,cost,i+1) + cost[0]

    idx = i
    while idx < len(days) and days[idx] < days[i] + 7 : idx += 1
    pass2 = ticket_min(days,cost,idx) + cost[1]

    idx = i
    while idx < len(days) and days[idx] < days[i] + 30 : idx += 1
    pass3 = ticket_min(days,cost,idx) + cost[2]

    memo[i] = min(pass1,pass2,pass3)
    return memo[i]

def ticket_tab(days,cost):
    dp = [ float('inf') for _ in range(len(days)+1)]
    dp[-1] = 0

    for i in range(len(dp)-2,-1,-1):
        pass1 = dp[i + 1] + cost[0]

        idx = i
        while idx < len(days) and days[idx] < days[i] + 7: idx += 1
        pass2 = dp[idx] + cost[1]

        idx = i
        while idx < len(days) and days[idx] < days[i] + 30: idx += 1
        pass3 = dp[idx] + cost[2]

        dp[i] =  min(pass1,pass2,pass3)

    return dp[0]

print(ticket_min([8,10],[2,7,20]))
print(ticket_tab([8,10],[2,7,20]))