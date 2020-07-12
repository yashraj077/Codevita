def permutations(l):
    if len(l)==0:
        return []
    if len(l)==1:
        return [l]
    current_permut = []
    for i in range(len(l)):
        m = l[i]
        remain_l = l[:i]+l[i+1:]

        for p in permutations(remain_l):
            current_permut.append([m] + p)
    return current_permut
if __name__ == "__main__":
    # data = list(input("Enter string to find permutation : "))
    a, b = map(int,input().split(" "))
    data = list(str(a))
    temp = []
    for p in permutations(data):
        x = ''
        for i in p:
            x = x + i
        temp.append(int(x))
    sortemp = sorted(temp)
   
    for i in sortemp:
        if i>b:
            print(i)
            break
    else:
        print(-1)
