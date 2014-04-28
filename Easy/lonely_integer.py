#! /usr/bin/env python
import sys

array_length = int(input())
array = [int(x) for x in raw_input().split(' ')]

if array_length == 1:
	print array[0]
	sys.exit()

array.sort()


i = 0

a, b, c = array[:3]
x, y, z = array[-3:]

if a != b and b == c:
	print a
elif x == y and y != z:
	print z

while i != array_length - 2:
	if array[i] != array[i + 1] and array[i + 1] != array[i + 2]:
		print array[i + 1]
		break
	else:
		i += 1
