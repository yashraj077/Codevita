a = input("")
b = int(input(""))

l = []

for _ in range(b):
    direct, index = map(str,input("").split())
    l.append([direct, index])

ans = ""

for i in l:
    if i[0] == "L":
        ans = ans + a[int(i[1])]
    elif i[0] == "R":
        ans = ans + a[-1*int(i[1])]

if ans in a:
    print("YES")
else:
    print("NO")
