# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:05:51 2020

@author: yash
"""

def isPrime(n) : 

	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True

	if (n % 2 == 0 or n % 3 == 0) : 
		return False

	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6

	return True

def count_Primes_nums(m, n):
    ctr = 0
    
    for num in range(m, n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr



start, end = map(int, input().split())
if start<=2:    
    l = [2]
else:
    l = []
for val in range(start, end + 1): 
	if val > 1: 
		for n in range(2, val//2 + 2): 
			if (val % n) == 0: 
				break
			else: 
				if n == val//2 + 1: 
					l.append(val)
#print(l)
temp = []
for k in range(len(l)):
    for x in range(len(l)):
        if k==x:
            continue
        else:
            if isPrime(int(str(l[k])+str(l[x])))==True and int(str(l[k])+str(l[x])) not in temp:
                temp.append(int(str(l[k])+str(l[x])))
temp.sort()

smallest = temp[0]
biggest = temp[-1]

FibArray = [smallest, biggest]
def fibonacci(n): 
	if n<=len(FibArray): 
		return FibArray[n-1] 
	else: 
		temp_fib = fibonacci(n-1)+fibonacci(n-2) 
		FibArray.append(temp_fib) 
		return temp_fib 

print(fibonacci(len(temp)))