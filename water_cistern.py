import math

r,h,s = map(int,input().split(","))
d,g = map(int,input().split(","))
# l = list(map(int,input().split(",")))
# m = list(map(int,input().split(",")))
# r = l[0]
# h = l[1]
# s = l[2]
# d = m[0]
# g = m[1]

if d>0:
    if s==d:
        ans = 2*3.14*r*g/360
        print(round(ans))
    if s!=d:
        le = 2*3.14*r*g/360
        ba = abs(s-d)
        ans = round(math.sqrt(le**2+ba**2))
        print(ans)
if d<0:
    if g==180:
        ans = s+r+abs(d)
        print(round(ans))
    if g!=180:
        a = math.sqrt((r**2)+(d**2)-(2*r*abs(d)*math.cos(math.radians(g))))
        ans = s+a
        print(round(ans))
