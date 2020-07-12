# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:19:57 2020

@author: yash
"""

def H(n):
    return n*((2*n)-1)

def T(N):
    return n*(n+1)//2


if __name__ == "__main__":
    try:
        a, b, c = map(int, input().split())

        Hl = []
        Tl = []
        n = 1
        count = c
        while True:
            if count==0:
                break
            temp1 = H(n)
            temp2 = T(n)
            if temp2 >=b:
                print("No number is present at this index")
                break
            else:

                if temp1 >=a:
                    Hl.append(temp1)
                    Tl.append(temp2)
                    if temp2 in Hl:
                        if count==1:
                            print(temp2)
                            break
                        else:
                            count-=1
            n+=1
    except:
        print("Invalid Input")