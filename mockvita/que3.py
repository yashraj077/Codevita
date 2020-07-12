# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:05:58 2020

@author: yash
"""

def patients():
    count = 0
    D = [31,28,31,30,31,30,31,31,30,31,30,31]
    for m in range(1, 13):
        for d in range(1, D[m-1]+1):
            count+=(6-m)**2 + abs(d-15)
    print(count)

if __name__ == "__main__":
#    r = int(input())
#    r1, r2 = map(int, input().split())
#    rev = int(input())
    patients()
    