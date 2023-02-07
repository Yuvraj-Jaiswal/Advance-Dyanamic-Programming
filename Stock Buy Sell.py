
def max_profit(arr):
    profit = 0
    minm = arr[0]
    for i in range(1,len(arr)):
        diff = arr[i]-minm
        profit = max(diff,profit)
        minm = min(arr[i],minm)
    return profit

print(max_profit([7,1,5,3,6,4]))
