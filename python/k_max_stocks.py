'''
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company
in chronological order and an integer k,
return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it,
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
'''


def find_differences(arr):
    totals = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                totals.append(arr[j] - arr[i])
    totals = sorted(totals, reverse=True)
    return totals


def find_max_profits(arr, k):
    totals = find_differences(arr)
    if len(totals) <= k:
        return sum(totals)
    else:
        return sum(totals[:k])


print(find_max_profits([5, 2, 4, 0, 1], 2))
