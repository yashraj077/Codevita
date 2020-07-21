import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
f = float(input())

lower_bound = min(x1, x2)
upper_bound = max(x1, x2)

while (round(lower_bound, 6)<round(upper_bound, 6)):
    mid = (lower_bound+upper_bound)/2.0
    upper_mid = (mid+upper_bound)/2.0
    lower_mid = (mid+lower_bound)/2.0

    lowertime = distance(x1, y1, lower_mid, 0)/f + distance(lower_mid, 0, x2, y2)
    uppertime = distance(x1, y1, upper_mid, 0)/f + distance(upper_mid, 0, x2, y2)

    if (lowertime<=uppertime):
        upper_bound = mid
    else:
        lower_bound = mid

print("{0:.6f}".format(upper_bound))
