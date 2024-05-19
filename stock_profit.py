def stock(arr):
    if (len(arr)<2):
        return 0,None,None,None,None
    
    min_price= float('inf')
    buy_price= 0
    sell_price= 0
    max_profit=0
    buy_day= sell_day=0

    for i, price in enumerate(arr):
        if price < min_price:
            min_price= price
            buy_day=i 
            buy_price= price
        profit= price- min_price
        if profit >max_profit:
            max_profit = profit
            sell_day=i
            sell_price= price

    if max_profit==0:
        return 0,None,None,None,None
    return max_profit, buy_day, sell_day, buy_price, sell_price


arr= list(map(int, input("Enter the prices of the stock:").split(',')))
profit, buy_day, sell_day,buy_price, sell_price = stock(arr)

if buy_day is not None and sell_day is not None:
    print(f"Buy on day {buy_day + 1} at price {arr[buy_day]}")
    print(f"Sell on day {sell_day + 1} at price {arr[sell_day]}")
    print(f"Maximum profit: {profit}")
else:
    print("No profit can be made")        

