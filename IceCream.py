#!/bin/python

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    sorted_cost=sorted(cost)
    cost_1, cost_2=0,0
    flag=0
    for i,c in enumerate(sorted_cost):
        low,high=0,len(cost)-1
        remaining=money-c
        while low<=high:
            mid=low+(high-low)/2
            if sorted_cost[mid]==remaining:
                cost_1=c
                cost_2=remaining
                flag=1
                break
            elif sorted_cost[mid]<remaining:
                low=mid-1
            else:
                high=mid+1
        if flag==1:
            break
    print cost_1, cost_2


        
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(cost, money)
