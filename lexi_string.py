N = int(input())

for _ in range(N):
    
    dict1 = {}
    
    s = input()
    # a = list(map(int, input().split("")))
    a = input()
    a = list(a)
    
    for index, i in enumerate(s):
        dict1[i] = index
    
    # bubble sort approach
    
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if dict1[a[i]]>dict1[a[j]]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    print(*a, sep="", end="\n")