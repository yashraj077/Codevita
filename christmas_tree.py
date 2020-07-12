
def generate(N, S, space):
    if S==1:
        start = 1
        count = 0
        N+=1
    else:
        start = 2
        count = 1
    for i in range(start, N+1):
        print(" "*space, end="")
        print(" "*(N-i), end="")
        print("*"*(i+count))
        count+=1

for _ in range(int(input())):
    N = int(input())
    
    if N<=1:
        print("You cannot generate christmas tree")
    elif N>20:
        print("Tree is no more")
    else:
        for i in range(N, 1, -1):
            if i==N:
                generate(N, 1, 0)
            else:
                generate(i+1, 0, (N-i))
        print(" "*N, end="")
        print("*")
        print(" "*N, end="")
        print("*")