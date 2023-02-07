def longestCommonSubstr(st1, st2, i=None, j=None, lcs=0):
    if i is None and j is None: i , j = len(st1)-1 , len(st2)-1
    if i < 0 or j < 0:return 0

    ans = 0
    a1 , a2 = 0 , 0
    if st1[i] == st2[j]:
        ans = 1+longestCommonSubstr(st1, st2, i - 1, j - 1, lcs + 1)
    else:
        a1 = longestCommonSubstr(st1, st2, i, j - 1, 0)
        a2 = longestCommonSubstr(st1, st2, i - 1, j, 0)

    lcs = max(a1, a2 ,ans)
    return lcs

print(longestCommonSubstr("abd","abcd"))