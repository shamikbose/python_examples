#!/bin/python

import math
import os
import random
import re
import sys

def findMedian(arr,d): #d is the number of trailing days
    bucketArray=[0]*201
    miniList=[0]*d
    for i in range(0,d):
        bucketArray[arr[i]]=bucketArray[arr[i]]+1
    position=0
    for i in range(0,d):
        
        while(bucketArray[position]==0):
            position=position+1
        miniList[i]=position
        bucketArray[position]=bucketArray[position]-1
    print miniList
    if d%2==0:
        return (miniList[d/2]+miniList[(d+1)/2])/2
    else:
        return miniList[d/2]
        

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count=0
    length=len(expenditure)
    for i in range(0,length-d-1):
        median=findMedian(expenditure[i:i+d],d)
        if expenditure[i+d]>=2*median:
            count=count+1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
