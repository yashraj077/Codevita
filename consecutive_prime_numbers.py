def check_prime(a):
    if a>1:
        for j in range(2,a):
            if a%j==0:
                return 0
        else:
            return 1

if __name__ == "__main__":
    a = int(input("Enter number : "))
    arr = []
    narr = []
    # [2, 3, 5, 7, 11, 13, 17]
    for i in range(2,a+1):
        if check_prime(i)==1:
            arr.append(i)
    for j in range(2,len(arr)-1):
        if sum(arr[0:j]) in arr:
            narr.append(sum(arr[0:j]))
    print(len(narr))