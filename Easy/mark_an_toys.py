#! /usr/bin/env python3

toys, money = (int(x) for x in input().split(' '))
prices = [int(x) for x in input().split(' ')]

prices = sorted(prices)
count = 0


for i in range(len(prices)):
	if money >= prices[i]:
		money = money - prices[i]
		count += 1

print(count)