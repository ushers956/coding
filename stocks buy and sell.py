def calculateProfit(arr,arr_size):

    profit = 0
    for i in range(1, arr_size):


        if arr[i] > arr[i-1]:

            profit += arr[i] - arr[i-1]

    return profit


prices = [635, 864, 247, 325, 257, 745, 245]

prices = calculateProfit(prices, len(prices))
print("max profit : ", prices)