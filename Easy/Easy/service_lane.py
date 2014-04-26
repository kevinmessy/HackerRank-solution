#! /usr/bin/env python

freeway, T = [int(x) for x in raw_input().split(' ')]
width = [int(x) for x in raw_input().split(' ')]

for i in range(0, T):
	enter, exit = [int(x) for x in raw_input().split(' ')]
	shortcut = width[enter: exit + 1]
	print min(shortcut) 