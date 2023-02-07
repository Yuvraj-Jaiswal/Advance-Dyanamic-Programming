
def longestcs(st1,st2,i=0,j=0,memo={}):
    if i >= len(st1) or j >= len(st2): return 0
    if f'{i},{j}' in memo:
        print(memo)
        return memo[f'{i},{j}']
    if st1[i]==st2[j]:
        lcs = 1 + longestcs(st1,st2,i+1,j+1,memo)
        memo[f'{i},{j}'] = lcs
        return lcs
    else:
        imax = longestcs(st1,st2,i+1,j,memo)
        jmax = longestcs(st1,st2,i,j+1,memo)
        lcs = max(imax,jmax)
        memo[f'{i},{j}'] = lcs
        return lcs

print(longestcs("abcde","def"))

import re
print(re.match("abc","abcded"))