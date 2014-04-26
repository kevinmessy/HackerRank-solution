#! /usr/bin/env python

T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    wrappers = A/B
    eat = wrappers
    while wrappers >= C1:
    	wrappers -= C1
    	wrappers += 1
    	eat += 1
    print eat 