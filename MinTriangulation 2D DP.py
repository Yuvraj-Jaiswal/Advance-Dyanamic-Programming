
def min_tiangualtion(value,i=None,j=None,memo={}):
    if i is None and j is None:i , j = 0 , len(value)-1
    if i+1 == j: return 0
    if f'{i},{j}' in memo : return memo[f'{i},{j}']
    ans = float('inf')
    for k in range(i+1,j):
        triltn_r = min_tiangualtion(value,i,k)
        triltn_l = min_tiangualtion(value,k,j)
        current = value[i]*value[j]*value[k]
        ans = min( current+triltn_r+triltn_l , ans)
    memo[f'{i},{j}'] = ans
    return ans

print(min_tiangualtion([1,2,8]))