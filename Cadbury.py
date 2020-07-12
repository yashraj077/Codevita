# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:42:01 2020

@author: yash
"""

if __name__ == "__main__":
#    H = int(input())
#    W = int(input())
    P, Q, R, S = map(int, input().split())
    
    
    count = 0
    for i in range(P, Q+1):
        for j in range(R, S+1):
            H=i
            W=j
#            print([H, W])
            while H!=W:
                if H>W:
                    H=H-W
#                    print(H, W)
                    count+=1
                else:
                    W=W-H
#                    print(H, W)
                    count+=1
            count+=1
    print(count)