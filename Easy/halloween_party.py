#! /usr/bin/env python

T = int(raw_input())

def slice():
	slices = int(raw_input())
	if slices % 2 == 0:
		slices = slices/2
		print slices * slices
	else:
		slices = slices - 1
		slices = slices/2
		print slices * (slices + 1)

for i in range(0, T):
	slice()