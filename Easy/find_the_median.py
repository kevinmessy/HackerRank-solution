#! /usr/bin/env python

array_size = int(input())
array = [int(x) for x in input().split(' ')]
array.sort()

answer = array[array_size//2:(array_size//2)+1]
print(answer.pop())