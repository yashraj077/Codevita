# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:00:10 2020

@author: yash
"""

def calc_revenue(rooms, tvs, room_traffic, r1, r2):
    revenue = 0
    
    for i in range(1, len(room_traffic)):
        if i<= (rooms-tvs):
            revenue+= room_traffic[i]*i*r2
        else:
            without_rooms = rooms-tvs
            with_tvs = i-without_rooms
            revenue = revenue + (without_rooms*room_traffic[i]*r2)+(with_tvs*room_traffic[i]*r1)
    return revenue

rooms = int(input())
r1, r2 = list(map(int, input().split()))
revenue_target = int(input())

DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
assert(sum(DAYS)==365)

occupancy = [0]*366

room_traffic = [0]*min(52+1, rooms+1)

for m in range(1, len(DAYS)):
    for d in range(1, DAYS[m]+1):
        patients = (6-m)**2+abs(d-15)
        curr_traffic = min(patients, rooms)
        room_traffic[curr_traffic]+=1

total_revenue = 0
possible = False
needed_tvs = 0

for tvs in range(0, rooms+1):
    curr_traffic = calc_revenue(rooms, tvs, room_traffic, r1, r2)
    if curr_traffic>=revenue_target:
        possible = True
        needed_tvs = tvs
        break
if possible:
    print(needed_tvs)
else:
    print(rooms)