#! /usr/bin/env python

test_cases = int(raw_input())


def solve(loops):
	season = 'moonsoon'
	height = 1
	count = int(loops)
	while count != 0:
		if season == 'moonsoon':
			height = height + height
			season = 'summer'
		elif season == 'summer':
			height = height + 1
			season = 'moonsoon'
		count -= 1
	print height


for i in xrange(1, test_cases + 1):
	solve(raw_input())