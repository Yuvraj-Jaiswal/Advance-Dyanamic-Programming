

def str_rep(st,dt,i=0,res=""):
    if i >= len(st) :
        is_same = "YES"
        for i in range(len(res)-1):
            if res[i]!=res[i-1]:
                is_same = "NO"
        return is_same

    if str_rep(st,dt,i+1,res+st[i]) == "YES": return "YES"
    if st[i] in dt:
        if str_rep(st,dt,i+1,res+dt[st[i]]) == "YES": return "YES"
    else:
        if str_rep(st, dt, i + 1, res + st[i]) == "YES": return "YES"
    return "NO"

st = "abccd"
lst1 = ["a","b"]
lst2 = ["b","c"]
dt = {lst1[0]:lst1[1],lst1[1]:lst1[0],lst2[0]:lst2[1],lst2[1]:lst2[0]}
print(str_rep(st,dt))

