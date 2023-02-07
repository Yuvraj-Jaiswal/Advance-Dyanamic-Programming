
def max_square(mat,i=0,j=0,max_sq=0):
    if i >= len(mat) or j >= len(mat[0]): return 0

    right1 = max_square(mat,i,j+1)
    diag1 = max_square(mat,i+1,j+1)
    bottom1 = max_square(mat,i+1,j)

    if mat[i][j] == 1:
        ans = 1 + min(right1,diag1,bottom1)
        max_sq = max(max_sq,ans)
        return max_sq

    else: return 0

grid = [[0,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]

print(max_square(grid))