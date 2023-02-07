
def stock_buy(arr,i=0,buy=False,memo={}):
    if i == len(arr):return 0
    if f'{i},{buy}' in memo :return memo[f'{i},{buy}']
    if buy:
        sellkaro = stock_buy(arr,i+1,buy=False) + arr[i]
        skipkaro = stock_buy(arr,i+1,buy)
        profit = max(sellkaro,skipkaro)
        memo[f'{i},{buy}'] = profit
        return profit
    else:
        buykaro = stock_buy(arr,i+1,buy=True) - arr[i]
        skipkaro = stock_buy(arr,i+1,buy)
        profit = max(buykaro, skipkaro)
        memo[f'{i},{buy}'] = profit
        return profit

print(stock_buy([7,1,5,3,6,4]))
