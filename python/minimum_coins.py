'''
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
'''

def minimum_coins(n):
	count = 0
	if n >= 25:
		count += (n // 25)
		n %= 25
	if n >= 10:
		count += (n // 10)
		n %= 10
	if n >= 5:
		count += (n // 5)
		n %= 5
	return count + n


if __name__ == '__main__':
	print(minimum_coins(16))