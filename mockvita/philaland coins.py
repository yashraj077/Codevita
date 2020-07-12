# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:46:42 2020

@author: yash
"""

# philaland coins

def decimalToBinary(n): 
	return bin(n).replace("0b", "") 
	
if __name__ == '__main__':
    for case in range(int(input())):
        n = int(input())
        print(len(decimalToBinary(n)))