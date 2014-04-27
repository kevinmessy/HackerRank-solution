#! /usr/bin/env python3

find = input()
array_size = int(input())
my_array = input().split(' ')

for i in range(array_size):
	if my_array[i] == find:
		print(i)